#from ..course_api.schedule import Schedule as usc_api_handle
from ..course_api.schedule import Schedule as usc_api_handle
from ..course_api.models import Course, SectionData, Instructor
from .courseCombo import CourseCombo, ClassSchedule
from .util import time_to_min
from .serializers import ComplexEncoder
from ..models import Professor
"""from course_api.schedule import Schedule as usc_api_handle
from course_api.models import Course, SectionData, Instructor
from serializers import ComplexEncoder
from courseCombo import CourseCombo, ClassSchedule
from util import time_to_min"""
import copy
import random
import json


NUM_COMBO_PER_COURSE = 5




class filter:
    def __init__(self, required_courses: list = None, blocked_times:list = None, available:bool = None, rmp:float = None, rmp_difficulty:float = None, units:int=None):
        self.required_courses = required_courses #priority is basically require class or no so its a dict of bools
        self.blocked_times = blocked_times
        self.want_available = available
        self.min_rmp = rmp
        self.max_rmp_difficulty = rmp_difficulty
        self.units_wanted = units  
class Optimizer:
    #subclass to hold prefrence information

        
    def __init__(self, course_ids:list, semester_id:str, required_courses: list = None, blocked_times:list = None, available:bool = None, rmp:float = None, rmp_difficulty:float = None, units:int=None):
        self.course_ids = course_ids
        self.semester_id = semester_id
        self.usc_api_handle = usc_api_handle()
        self.prefrences = filter(required_courses, blocked_times, available, rmp, rmp_difficulty, units)


    

    def set_rmp(self, course):
        for section in course.sections:
            for instructor in section.instructors:
                name = instructor.first_name + " " + instructor.last_name
                rmp_profs = Professor.objects.filter(name=name)
                if len(rmp_profs) == 0:
                    instructor.rating = None
                    instructor.num_ratings = None
                    instructor.difficulty = None
                else:
                    rmp_prof = rmp_profs[0]
                    instructor.rating = float(rmp_prof.rating)
                    instructor.num_ratings = int(rmp_prof.num_ratings)
                    instructor.difficulty = float(rmp_prof.difficulty)


    #function to create course objects for list of class names
    def get_courses(self) -> dict:
        id_to_course = {}
        for id in self.course_ids:
            print(id)
            course = self.usc_api_handle.get_course(course_id=id, semester_id=self.semester_id)
            self.set_rmp(course)
            id_to_course[id] = course
        return id_to_course

    #function to generate combos for each section group 
    def generate_combos(self, course, group_sections:list) -> list:
        #generate combos
        combinations = []
        lectures = []
        labs = []
        discussions = []
        quizes = []
        for section in group_sections:
            if section.type == "Lec" or section.type == "Lec-Lab" or section.type == "Lec-Dis":
                lectures.append(section)
            elif section.type == "Lab":
                labs.append(section)
            elif section.type == "Dis":  # Discussion
                discussions.append(section)
            else:  # Quiz (Qz)
                quizes.append(section)
        if(len(lectures) == 0):
            labs = [None]
        if(len(labs) == 0):
            labs = [None]
        if(len(discussions) == 0):
            discussions = [None]   
        if(len(quizes) == 0):
            quizes = [None]
    
        for lecture in lectures:
            for lab in labs:
                for discussion in discussions:
                    for quiz in quizes:
                        combo = CourseCombo(course, lecture, lab, discussion, quiz)
                        combinations.append(combo)
        random.shuffle(combinations)
        return combinations[0:NUM_COMBO_PER_COURSE]

    #function to generate list of unique course combo objects 
    #that has each required section a student needs to take at once
    def generate_single_course_combos(self, course) -> list:
        #initialize sections
        #TODO need to seperate different lectures
        #define what type of course this is
        #type 1: all lecture sections can be taken interchangeably
        #type2: lab/quiz/disc can only be taken with specific lecture sections
        
        #find all lecture-lab/disc/quiz groups
        sections = course.sections
        section_group_indexes = [0]
        last_section = sections[0]
        for i in range(1,len(sections)):
            #check if last section wasnt a lecture and this one is a lecture
            if  last_section.type != "Lec" and last_section.type != "Lec-Lab" and last_section.type != "Lec-Dis" and \
                (sections[i].type == "Lec" or sections[i].type == "Lec-Lab" or sections[i].type == "Lec-Dis"):
                    section_group_indexes.append(i)
            last_section = sections[i]
        section_group_indexes.append(len(sections))

        combinations = []
        for i in range(len(section_group_indexes)-1):
            section_group = sections[section_group_indexes[i]: section_group_indexes[i+1]]
            combinations += self.generate_combos(course, section_group)
        return combinations



    #helper function to check if a time overlaps
    def overlaps(self, current_section_time, prev_section_time):
        #check if on same day
        #print(f"{current_section_time} {prev_section_time}")
        day_overlaps = False
        for day in current_section_time[0]:
            if day in prev_section_time[0]:
                day_overlaps = True
        if(day_overlaps == False):
            return False
        #check new-end is before old-start
        if(time_to_min(current_section_time[2]) < time_to_min(prev_section_time[1])):
            return False
        #check old-end is before new-start
        if(time_to_min(prev_section_time[2]) < time_to_min(current_section_time[1])):
            return False
        return True
                    
    #function to see if a CourseCombo overlaps times 
    #with any CourseCombo in prev_combos
    def time_conflicts(self, combo, prev_combos):
        #save time of current course combo in temp variable
        current_time_combined = combo.times
        #loop through each previous combo and check if time intersects
        for i, prev_combo in enumerate(prev_combos):
            prev_time_combined = prev_combo.times
            for current_section_time in current_time_combined:
                for prev_section_time in prev_time_combined:
                    #if overlap
                    if self.overlaps(current_section_time, prev_section_time):
                        return True
        return False


    #ill represent a schedule using 2d aray
    #function to create all possible schedules
    #all schedule where time doesn't conflict
    def generate_schedules(self):
        #list of list of CourseCombo
        possible_combos = []
        #id_to_course maps course ids to course objects
        #course objects contain all sections under that course
        id_to_course = self.get_courses()
        courses = list(id_to_course.values())
        
        #recursive helper function
        def combinations(temp_courses, prev_combos):
            #base case if number of units matches number wanted
            units = 0
            for combo in prev_combos:
                units += combo.units
            if(units == self.prefrences.units_wanted):
                sched = ClassSchedule(course_combos=prev_combos, semester=self.semester_id)
                possible_combos.append(sched)
                return
            #base case if out of clases or over units wanted
            if(len(temp_courses) == 0 or units > self.prefrences.units_wanted):
                return
            #get current course and all its lec/lab/disc/qz combos
            for i, val in enumerate(temp_courses):
                current_course = val
                course_combos = self.generate_single_course_combos(current_course)
                #loop through each option
                for combo in course_combos:
                    #check for any time conflicts
                    if self.time_conflicts(combo, prev_combos) == False:
                        new_combos = copy.deepcopy(prev_combos)
                        new_combos.append(combo)
                        combinations(temp_courses[i+1:], new_combos)   
        combinations(courses, [])
        return possible_combos

    #check if both the user cares about availability
    #if so: check all classes are available
    def check_available(self, schedule):
        def section_full(courseSection):
            return courseSection is not None \
                and courseSection.get_available_spots() <= 0
        
        if(self.prefrences.want_available is None or self.prefrences.want_available is False):
            return True
        
        courses = schedule.course_combos
        for courseCombo in courses:
            if section_full(courseCombo.lecture) \
                or section_full(courseCombo.lab) \
                or section_full(courseCombo.discussion) \
                or section_full(courseCombo.quiz):
                    return False
        return True
    
    #check if schedule has all courses required by user
    def check_prioritized(self, schedule):
        if(self.prefrences.required_courses is None):
            return True
        required_courses = self.prefrences.required_courses
        courses = schedule.course_combos
        #count number of required courses are selected
        selected_required_courses = 0
        for class_combo in courses:
            course = class_combo.course
            if course.scheduled_course_id in required_courses or course.published_course_id in required_courses:
                selected_required_courses+=1
        #throw if somehow count more required courses then required
        if selected_required_courses > len(required_courses):
            raise RuntimeError
        #return whether this schedule has all required courses
        else:
            return selected_required_courses == len(required_courses)

    def check_rmp_score_difficulty(self, schedule):
        if(self.prefrences.blocked_times is None):
            return True
        #need to account for when prof doesnt have rmp
        class_combos = schedule.course_combos
        min_rmp = self.prefrences.min_rmp
        max_diff = self.prefrences.max_rmp_difficulty
        for class_combo in class_combos:
            prof = class_combo.get_professor()
            if prof.rating == None or prof.difficulty == None or min_rmp == None or max_diff == None:
                continue
            if(prof.rating < min_rmp and prof.difficulty > max_diff):
                return False
        return True
    
    #check if courses overlap with any times 
    #blocked out by user
    def check_blocked_time(self, schedule):
        if(self.prefrences.blocked_times is None):
            return True
        class_combos = schedule.course_combos
        blocked_times = self.prefrences.blocked_times

        for class_combo in class_combos:
            for class_time in class_combo.times:
                for blocked_time in blocked_times:
                    if(self.overlaps(blocked_time, class_time)):
                        return False
        return True
    
    def check_units(self, schedule):
        if(self.prefrences.units_wanted is None):
            return True
        return schedule.units == self.prefrences.units_wanted

        
        
    #filter possible combos
    def filter_combinations(self, possible_combos):
        filtered_schedule = []
        #loop through each schedule
        for schedule in possible_combos:
            #keep track on whether to filter
            #make sure all prioritized courses are selected
            #check rmp of lecture (if it exists)
            #check availability of all course sections(ifthey exist)
            #check overlap block times
            #check if num units matches
            if self.check_available(schedule) \
               and self.check_blocked_time(schedule) \
               and self.check_prioritized(schedule) \
               and self.check_rmp_score_difficulty(schedule): 
                filtered_schedule.append(schedule)
        return filtered_schedule
    

  
            


if __name__ == "__main__":
    import time
    start_time = time.time()

    

    id = "20231"
    course_ids = ["MATH-125", "CSCI-103", "LING-115", "CSCI-170"]
    optimizer = Optimizer(course_ids,id,units=16, available=True, rmp=3, rmp_difficulty=4)
    #courses = optimizer.get_courses()
    #print("--- %s seconds rmp ---" % (time.time() - start_time))
    #course_1 = list(courses.values())[0]
    #course_combos = optimizer.generate_single_course_combos(course_1)
    """for course in courses.values():
        combos = optimizer.generate_single_course_combos(course)
        for combo in combos:
            print(combo)
            print(str(combo.get_professor()))"""
    scheds = optimizer.generate_schedules()
    scheds = optimizer.filter_combinations(scheds)
    print("--- %s seconds optimizer ---" % (time.time() - start_time))
    schedule1 = scheds[0]
    print( json.dumps(scheds, cls=ComplexEncoder, indent=4))
    #print(json.dumps(schedule1.reprJSON(), default=ComplexEncoder))
    """for sched in scheds:
        combos = sched.course_combos
        for combo in combos:
            print(combo, "")
            print(combo.lecture.title, "")
            if(len(combo.lecture.instructors)!=0):
                print(combo.lecture.instructors[0].get_name(), "")
        print()"""
    print(len(scheds))
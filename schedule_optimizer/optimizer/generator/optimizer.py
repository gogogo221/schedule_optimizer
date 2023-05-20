from uscschedule import Schedule as usc_api_handle
from .courseCombo import CourseCombo, ClassSchedule
from .util import time_to_min
import copy
import random

NUM_COMBO_PER_COURSE = 5

class Optimizer:
    #subclass to hold prefrence information
    class filter:
        def __init__(self, required_courses: list = None, blocked_times:list = None, available:bool = None, rmp:float = None, rmp_difficulty:float = None, units:int=None):
            self.required_courses = required_courses #priority is basically require class or no so its a dict of bools
            self.blocked_times = blocked_times
            self.want_available = available
            self.rmp = rmp
            self.rmp_difficulty = rmp_difficulty
            self.units = units  
        
    def __init__(self, course_ids:list, semester_id:str, required_courses: list = None, blocked_times:list = None, available:bool = None, rmp:float = None, rmp_difficulty:float = None, units:int=None):
        self.course_ids = course_ids
        self.semester_id = semester_id
        self.usc_api_handle = usc_api_handle()
        self.prefrences = filter(required_courses, blocked_times, available, rmp, rmp_difficulty, units)

    #function to create course objects for list of class names
    def get_courses(self) -> dict:
        id_to_course = {}
        for id in self.course_ids:
            id_to_course[id] = self.usc_api_handle.get_course(course_id=id, semester_id=self.semester_id)
        return id_to_course

    #function to generate list of unique course combo objects 
    #that has each required section a student needs to take at once
    def generate_single_course_combos(self, course) -> list:
        #initialize sections
        #TODO need to seperate different lectures
        lectures = []
        labs = []
        discussions = []
        quizes = []
        for section in course.sections:
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
    
        #generate combos
        combinations = []
        for lecture in lectures:
            for lab in labs:
                for discussion in discussions:
                    for quiz in quizes:
                        combo = CourseCombo(course, lecture, lab, discussion, quiz)
                        combinations.append(combo)
        random.shuffle(combinations)
        return combinations[0:NUM_COMBO_PER_COURSE]


    #helper function to check if a time overlaps
    def overlaps(self, current_section_time, prev_section_time):
        #check if on same day
        #print(f"{current_section_time} {prev_section_time}")
        if(current_section_time[0] != prev_section_time[0]):
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
            if(units == self.prefrences.units):
                sched = ClassSchedule(course_combos=prev_combos)
                possible_combos.append(sched)
                return
            #base case if out of clases or over units wanted
            if(len(temp_courses) == 0 or units > self.prefrences.units):
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
        
        courses = schedule.classes
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
        courses = schedule.classes
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
        if(self.prefrences.units is None):
            return True
        return schedule.units == self.prefrences.units

        
        
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
            print(schedule.units)
            if self.check_available(schedule) \
               and self.check_blocked_time(schedule) \
               and self.check_prioritized(schedule) \
               and self.check_rmp_score_difficulty(schedule): 
                filtered_schedule.append(schedule)
        return filtered_schedule
    

  
            


if __name__ == "__main__":

    id = "20233"
    course_ids = ["CSCI-353", "CSCI-356", "CSCI-360", "CSCI-170", "LING-115", "WRIT-150"]
    pref = filter(units=16)
    optimizer = Optimizer(course_ids,id,pref)
    scheds = optimizer.generate_schedules()
    scheds = optimizer.filter_combinations(scheds)
    for sched in scheds:
        combos = sched.course_combos
        for combo in combos:
            print(combo, "")
            print(combo.lecture.title, "")
            if(len(combo.lecture.instructors)!=0):
                print(combo.lecture.instructors[0].get_name(), "")
        print()
    print(len(scheds))
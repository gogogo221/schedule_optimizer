#maybe dont bother with the 2d array 
# and instaed just keep track of list of day + times
#since im just checking for overlap with each time
#TODO dont redo to not use 2d array



class CourseCombo:
    def __init__(self, course, lecture, lab, discussion, quiz):
        self.course = course
        self.lecture = lecture
        self.lab = lab
        self.discussion = discussion
        self.quiz = quiz
        
        self.units = int((self.lecture.units if self.lecture is not None else self.course.units)[0])
        #assumes labs/disc doesn't overlap with lecture quiz
        self.times = []
        if self.lecture is not None:   
            self.times.append(self.lecture.compile_session_time())
        if self.lab is not None:   
            self.times.append(self.lab.compile_session_time())
        if self.discussion is not None:   
            self.times.append(self.discussion.compile_session_time())
        if self.quiz is not None:   
            self.times.append(self.quiz.compile_session_time())

    def __str__(self):
        return f"{self.times}"

    def get_professor(self):
        if self.lecture is not None:
            if len(self.lecture.instructors) >0:
                return self.lecture.instructors[0]
            else:
                return None
            
    def reprJSON(self):
        retval =  {
                    "course":self.course,
                    "sessions": [
                                    #TODO LATER
                                ]
                }
        if self.lecture is not None:
            retval["sessions"].append(self.lecture)
        if self.lab is not None:
            retval["sessions"].append(self.lab)
        if self.discussion is not None:
            retval["sessions"].append(self.discussion)
        if self.quiz is not None:
            retval["sessions"].append(self.quiz)
        return retval
        




class ClassSchedule:
    def __init__(self, course_combos=list, semester=str):
        self.course_combos = course_combos
        #count units in the schedule
        self.units = 0
        self.semester = semester
        for course_combo in self.course_combos:
            self.units += course_combo.units
        
    def reprJSON(self):
        retval={
                    "units":self.units,
                    "course_combos":self.course_combos,
                    "semester":self.semester
               }
        return retval




        
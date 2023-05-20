import pandas as pd
import numpy as np


#maybe dont bother with the 2d array 
# and instaed just keep track of list of day + times
#since im just checking for overlap with each time
#TODO dont redo to not use 2d array

class Time:
    def __init__(self, day, start, end):
        self.day = day
        self.start = start
        self.end = end
    
    def __str__(self):
        return f"{self.day} {self.start} {self.end}"

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


class ClassSchedule:
    def __init__(self, course_combos=list):
        self.course_combos = course_combos
        #count units in the schedule
        self.units = 0
        for course_combo in self.course_combos:
            self.units += course_combo.units



        
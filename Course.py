from threading import *
import time
from users import *
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday']

class Course(object):
    '''
    A class to represent a course including the students and timetable
    '''
    def __init__(self: Course,admin: Admin ,tutor_times: TutorTimes,name: str) -> None:
        
        # create the private variables
        self._admins = set()
        self._students = set()
        self._admins.add(admin)
        self._name = name
        
        self._TutorEvents = set()
        self._tutor_times = tutor_times
        
        # initialize 
        change_Event = Event()
        time_Event = Event()
        
        self._time_monitor = TimeMonitor(self,time_event)
        self._change_monitor = Changemonitor(self,change_event)
        
        # start the threads
        self._time_monitor.start()
        self._change_monitor.start()        
        
    def add_student(self,student):
        self._students.add(student)
    
    def remove_student(self,student):
        self._students.difference_update(set(student))
        
    def add_admin(self,admin):
        self._admins.add(student)

    def remove_admin(self,admin):
        self._admins.difference_update(set(admin))

    def add_TutorEvent(self,day,TutorEvent):
        self._change_event.set()
        self._TutorEvents.add(TutorEvent)

    def remove_TutorEvent(self,day,TutorEvent):
        self._TutorEvents.difference_update(set(TutorEvent))
        self._change_event.set()

    def notify(self,message):
        self._tutor_times.notify(students,message)
    
    def get_TutorEvents():
        return self._TutorEvents()       
    
    def get_name():
        return self._name

class TutorEvent:
    
    def __init__(self, start_time, end_time, room, name):
        self._start = start_time
        self._end = end_time
        self._room = room
        self._name = name
        self._already_notified = False
        
    def get_name(self):
        return self._name
    
    def get_room(self):
        return self._room
    
    def edit_start(self,new_time):
        self._start = new_time
        
    def edit_end(self,new_time):
        self._end = new_time

    def during_TutorEvent(self):
        '''
        checks wether the current time is in the middle of an TutorEvent
        '''
        curr_time = int(round(time.time() * 1000))
        output = False
        if(self._start <= curr_time <= end_time 
           and not self._currently_notified):
            output = True
            self._currently_notified = True
        return output

    def time_left(self):
        curr_time = int(round(time.time() * 1000))
        return self._end - curr_time

class TimeMonitor(Thread):
    '''
    monitors wether it currently is an

    '''

    def __init__(self,course,event):
        Thread.__init__(self)
        self._course = course
        self._event = event
        
    def run(self):
        while True:
            # 45 seconds in millis
            longest_wait = 45000
            self._event.wait(longest_wait/1000)
            message = 'There are office hours being held in:'
            for TutorEvent in self._course.get_TutorEvents():
                if(TutorEvent.during_TutorEvent()):
                    message += TutorEvent.get_room()
                    message+= ','
                    curr_length = TutorEvent.time_left()
                    # choose the longest wait to prTutorEvent spam
                    if(longest_wait < curr_length):
                        longest_wait = curr_length
            self._event.clear()
            self._event.wait(longest_wait/1000)    
            
                    
class ChangeMonitor(Thread):
    '''
    monitors wether an update has been made to the TutorEvents
    '''
    def __init__(self,course,event):
        Thread.__init__(self)
        self._course = course
        self._event = event
    def run(self):
        message = 'An instructor has modified a course.'
        while True:
            self._event.wait()
            self._course.notify(message)
            self._event.clear()

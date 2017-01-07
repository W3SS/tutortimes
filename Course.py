from thread import *
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
        
        self._events = set()
        self._tutor_times = tutor_times
        # initialize 
        self._time_monitor = TimeMonitor(self)
        self._change_monitor = Changemonitor(self)
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

    def add_event(self,day,event):
        self._monitor.set()
        self._events.add(event)

    def remove_event(self,day,event):
        self._events.difference_update(set(event))
        self._monitor.set()

    def notify(self,message):
        self._tutor_times.notify(students,message)
    
    def get_events():
        return self._events()       
    
    
    def get_name():
        return self._name

class Event:
    
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

    def during_event(self):
        '''
        checks wether the current time is in the middle of an event
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

    def __init__(self,course):
        Thread.__init__(self)
        self._course = course
        
    def run():
        while True:
            # 45 seconds in millis
            longest_wait = 45000
            self.wait(longest_wait/1000)
            message = 'There are office hours being held in:'
            for event in self._course.get_events():
                if(event.during_event()):
                    message += event.get_room()
                    message+= ','
                    curr_length = event.time_left()
                    # choose the longest wait to prevent spam
                    if(longest_wait < curr_length):
                        longest_wait = curr_length
            self.wait(longest_wait/1000)    
            
                    
class ChangeMonitor(Thread):
    '''
    monitors wether an update has been made to the events
    '''
    def __init__(self,course):
        Thread.__init__(self)
        self._course = course
           
    def run():
        message = 'An instructor has modified a course.'
        while True:
            self.wait()
            self._course.notify(message)
"""Task object that can be stored and displayed"""
from datetime import datetime
from CONSTANTS import *

class Task():

    def __init__(self, description, status, priority, utc):
        """Create a new instance of a task
        [description] is the name of the task 
        [status] is either incomplete, complete, or blocked
        [priority] is an integer from 1 - 5, with 1 being the highest
        """
        self.description = description
        self.status = status
        self.created_on = utc
        self.completed_on = None
        self.priority = priority
        self.active = True

    
    def get_status(self):
        return self.status

    def get_description(self):
        return self.description
    
    def get_priority(self):
        return self.priority
    
    def set_status(self, status, utc):
        self.status = status
        if status == INPROGRESS:
            self.completed_on = None
        elif status == COMPLETE:
            self.completed_on = utc

    def set_description(self, description):
        self.description = description

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def set_priority(self, priority): 
        self.priority = priority
    
    def set_completed(self, utc):
        self.set_status(COMPLETE)
        self.completed_on = utc

    def __str__(self):
        ret = self.description
        if self.priority:
            ret += f" [priority: {self.priority}]"
        if self.completed_on:
            ret += f" [completed on: {self.generateDate(self.completed_on)}]"
        return ret
    
    def generateDate(self, utc):
        """returns string of date"""
        full_date = utc.strftime("%d-%b-%Y (%H:%M:%S.%f)") #18-Nov-2018 (08:34:58.674035)
        date = full_date.split(" ")[0] #18-Nov-2018
        date = date.split("-") #(18, Nov, 2018))
        return f"{date[1]} {date[0]}, {date[2]}"
    
    
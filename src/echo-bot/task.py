"""Task object that can be stored and displayed"""
from datetime import datetime
from CONSTANTS import *

class Task():

    def __init__(self, description, status, priority):
        """Create a new instance of a task
        [description] is the name of the task 
        [status] is either incomplete, complete, or blocked
        [priority] is an integer from 1 - 5, with 1 being the highest
        """
        self.description = description
        self.status = status
        self.created_on = datetime.now()
        self.completed_on = None
        self.priority = priority
    
    def get_status(self):
        return self.status

    def get_description(self):
        return self.description
    
    def get_priority(self):
        return self.priority
    
    
    def set_status(self, status):
        self.status = status

    def set_description(self, description):
        return self.description

    def set_priority(self, priority): 
        return self.priority
    
    def set_completed(self):
        self.set_status(COMPLETE)
        self.completed_on = datetime.now()

    def __str__(self):
        return f"{self.description}, Priority: {self.priority}"
    
    
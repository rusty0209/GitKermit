"""Task object that can be stored and displayed"""
from datetime import datetime

class Task():

    def __init__(self, description, status, priority):
        """Create a new instance of a task
        [description] is the name of the task 
        [status] is either incomplete, complete, or blocked
        [priority] is either low, medium or high 
        """
        self.description = description
        self.status = status
        self.created_on = datetime.now()
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

    def __str__(self):
        return f"Task: {self.description}, Status: {self.status}"
    
    
"""Task Manager manages the to-do list and includes features, such as adding tasks and removing tasks 
    from the list """
from collections import defaultdict
from todo_errors import InvalidCommandError, NoSlashError
from CONSTANTS import *
from task import Task

class TaskManager(): 

    def __init__(self):
        self.tasks = defaultdict(list)
        #self.standup_times = {}
    
    def addTask(self, user, task): 
        self.tasks[user].append(task)
        return f"Added task {task}"
        
    def removeTask(self, user, task):
        self.tasks[user].remove(task)
        return f"Removed task {task}"

    # def printTask(self, user):
    #     self.tasks[user].print(task)

    def helpUser(self): 
        return HELPERMSG
    
    ### TODO: ARE YOU SURE YOU WANT TO DELETE THE TASK?
    def clearTask(self, user): 
        self.tasks[user] = []

    def handleCommand(self, full_command, user_id):
        """
        full_command = /todo I did this
        command = todo
        task_name = I did this
        """
        return_msg = ""
        if (full_command[0] == "/"): 
            full_command = full_command.split(" ", 1)
            command = full_command[0][1:]

            if len(full_command) > 1:
                task_name = full_command[1]
                task = Task(task_name, INPROGRESS, 0)

            if command == "help": 
                return_msg = self.helpUser()
            elif command == "todo":
                return_msg = self.addTask(user_id, task)
            elif command == "completed":
                return_msg = self.removeTask(user_id, task)
            elif command == "show":
                return_msg = self.displayTasks(user_id)

            else:
                raise InvalidCommandError(full_command, INVALIDMSG)
        else: 
            raise NoSlashError(full_command, NOSLASHMSG)
            
        return return_msg

    def displayTasks(self, user):
        string = "show\n"
        for i in range(len(self.tasks[user])):
            string += f"{i}: {self.tasks[user][i]} \n"
        return string


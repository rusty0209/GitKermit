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
    
    def addTask(self, user, description, priority=None):
        task = Task(description, INPROGRESS, priority) 
        self.tasks[user].append(task)
        return f"Added task {task}"
  
    def removeTask(self, user, arg):
        """deletes task"""
        task_idx = self.getTaskIndex(user, arg)
        task = self.tasks[user][task_idx]
        del self.tasks[user][task_idx]
        return f"Removed task {task}"

    def completeTask(self, user, arg):
        """marks task as complete"""
        task_idx = self.getTaskIndex(user, arg)
        self.tasks[user][task_idx].status = COMPLETE
        task = self.tasks[user][task_idx]
        return f"Marked task {task} as complete"

    def getTaskIndex(self, user, arg):
        if arg.isnumeric():
            if len(self.tasks[user]) > int(arg):
                return int(arg)
        else:
            for index, task in enumerate(self.tasks[user]):
                if task.description == arg:
                    return index
        return -1
    
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
        title = ""
        return_msg = ""
        if (full_command[0] == "/"): 
            full_command = full_command.split(" ", 1)
            command = full_command[0][1:]

            if len(full_command) > 1:
                task_name = full_command[1]

            if command == "help":
                title = "Help" 
                return_msg = self.helpUser()
            elif command == "todo":
                title = "Task Added"
                if "priority=" in task_name:
                    return_msg = self.addTask(user_id, task_name[0:-11], int(task_name[-1]))
                else:
                    return_msg = self.addTask(user_id, task_name)
            elif command == "complete":
                title = "Task Completed!"
                return_msg = self.completeTask(user_id, task_name)
            elif command == "remove":
                title = "Task Removed"
                return_msg = self.removeTask(user_id, task_name)
            elif command == "show": 
                title = "Incomplete Tasks"
                return_msg = self.displayTasks(user_id, INPROGRESS)
                if "task_name" in locals():
                    if task_name == "completed":
                        title = "Completed Tasks" 
                        return_msg = self.displayTasks(user_id, COMPLETE)
                    if task_name == "all":
                        title = "All Tasks" 
                        return_msg = self.displayStandUpHelper(user_id)
                    else: 
                        raise InvalidCommandError(full_command, INVALIDMSG)
            elif command == "standup": 
                title = "StandUp Buddy"
                return_msg = self.displayStandUpHelper(user_id)
            else:
                raise InvalidCommandError(full_command, INVALIDMSG)
        else: 
            raise NoSlashError(full_command, NOSLASHMSG)
        
        return title, return_msg

    def displayTasks(self, user, status):
        string = ""
        for i in range(len(self.tasks[user])):
            if self.tasks[user][i].status == status:
                string += f"{i}: {self.tasks[user][i]} \n\n"
        return string
    
    def displayStandUpHelper(self, user): 
        complete = self.displayTasks(user, COMPLETE)
        incomplete = self.displayTasks(user, INPROGRESS)
        return f"Completed Tasks: \n\n {complete} \n\n Incomplete Tasks:\n\n {incomplete}"
"""Task Manager manages the to-do list and includes features, such as adding tasks and removing tasks 
    from the list """
from collections import defaultdict
from todo_errors import InvalidCommandError, NoSlashError
from CONSTANTS import *
from task import Task
from datetime import timedelta
import string

class TaskManager(): 

    def __init__(self):
        self.tasks = defaultdict(list)
        self.commands = ["todo", "complete", "standup", "remove", 
                         "show", "help", "priority", "clear", "tomorrow", 
                         "edit", "status", "description"]
        #self.standup_times = {}
    
    def addTask(self, user, description, utc, priority=None):
        for t in self.tasks[user]:
            t.set_inactive()
        task = Task(description, INPROGRESS, priority, utc)
        self.tasks[user].append(task)
        return f"Added task {task}"
  
    def removeTask(self, user, arg):
        """deletes task"""
        task_idx = self.getTaskIndex(user, arg)
        task = self.tasks[user][task_idx]
        del self.tasks[user][task_idx]
        return f"Removed task {task}"

    def completeTask(self, user, arg, utc):
        """marks task as complete"""
        task_idx = self.getTaskIndex(user, arg)
        self.tasks[user][task_idx].set_status(COMPLETE, utc)
        task = self.tasks[user][task_idx]
        return f"Marked task {task} as complete"

    def markForEdit(self,user,arg):
        task_idx = self.getTaskIndex(user, arg)
        if task_idx > -1:
            for t in self.tasks[user]:
                t.set_inactive()
            self.tasks[user][task_idx].set_active()
            return self.tasks[user][task_idx]
        return None

    def editTask(self,user,arg):
        task = self.markForEdit(user, arg)
        if task:
            return f"""Now editing task {task.description}. Use '/priority [priority]', '/status [status]', 
                       or '/description [description]' to edit respective attributes."""

    def changeDescription(self, user, description):
        for i, task in enumerate(self.tasks[user]):
            if task.active:
                task_idx = i
                break
        oldDesc = self.tasks[user][task_idx].get_description()
        self.tasks[user][task_idx].set_description(description)
        task = self.tasks[user][task_idx]
        return f"Changed task {oldDesc} to {description}"

    def changePriority(self, user, priority):
        task_idx = -1
        for i, task in enumerate(self.tasks[user]):
            if task.active:
                task_idx = i
                break
        print(priority)
        oldPrio = self.tasks[user][task_idx].get_priority()
        self.tasks[user][task_idx].set_priority(priority)
        print(self.tasks[user][task_idx].get_priority())
        task = self.tasks[user][task_idx]
        return f"Changed priority of task {task.description} from {oldPrio} to {priority}"

    def changeStatus(self, user, status, utc):
        for i, task in enumerate(self.tasks[user]):
            if task.active:
                task_idx = i
                break
        oldStatus = self.tasks[user][task_idx].get_status()
        self.tasks[user][task_idx].set_status(status, utc)
        task = self.tasks[user][task_idx]
        return f"Changed status of task {task.description} from {oldStatus} to {status}"

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
    def clearTasks(self, user): 
        self.tasks[user] = []

    def handleCommand(self, full_command, user_id, utc):
        """
        full_command = /todo I did this
        command = todo
        task_name = I did this
        """
        title = ""
        return_msg = ""
        type = ""
        task_name = ""
        print(full_command)
        if (full_command[0] == "/"): 
            split_command = full_command.split(" ", 1)
            command = split_command[0][1:]

            if len(split_command) > 1:
                task_name = split_command[1]

            if command == "help":
                title = "Help" 
                return_msg = self.helpUser()
                type = "help"
            elif command == "todo":
                title = "Task Added"
                if "priority=" in task_name:
                    return_msg = self.addTask(user_id, task_name[0:-11], utc, int(task_name[-1]))
                    type = "todopriorityset"
                else:
                    return_msg = self.addTask(user_id, task_name, utc)
                    type = "todo"
            elif command == "complete":
                title = "Task Completed!"
                return_msg = self.completeTask(user_id, task_name, utc)
                type = "complete"
            elif command == "remove":
                title = "Task Removed"
                return_msg = self.removeTask(user_id, task_name)
                type = "remove"
            elif command == "edit":
                title = "Edit Task"
                return_msg = self.editTask(user_id, task_name)
                if return_msg is None:
                    return_msg = "Did not find task to edit"
                type = "edit"
            elif command == "show": 
                title = "Incomplete Tasks"
                return_msg = self.displayTasks(user_id, INPROGRESS, utc)
                type = "show"
                if task_name:
                    if task_name == "completed":
                        title = "Completed Tasks" 
                        return_msg = self.displayTasks(user_id, COMPLETE, utc)
                    elif task_name == "all":
                        title = "All Tasks" 
                        return_msg = self.displayStandUpHelper(user_id, utc)
                    else: 
                        raise InvalidCommandError(full_command, INVALIDMSG)
            elif command == "priority": 
                title = "Priority Change"
                return_msg = self.changePriority(user_id, task_name)
                type = "priority"
            elif command == "status": 
                title = "Status Change"
                return_msg = self.changeStatus(user_id, task_name, utc)
                type = "status"
            elif command == "description": 
                title = "Description Change"
                return_msg = self.changeDescription(user_id, task_name)
                type = "description"
            elif command == "standup": 
                title = "StandUp Buddy"
                return_msg = self.displayStandUpHelper(user_id, utc, True)
                type = "standup"
            elif command == "tomorrow":
                title = ""
                return_msg = ""
                type = None
            elif command == "clear":
                title = "Are you sure?"
                return_msg = "This can't be undone."
                type = "are you sure"
            elif command == "clearyesimsure":
                title = "Cleared All Tasks"
                return_msg = self.clearTasks(user_id)
                type = "clear"
            else:
                for i in self.edits1(command):
                    if i in self.commands:
                        return f"Command not found. Did you mean '/{i}'?", YOUNEEDHELP, "spelling"
                for i in self.edits2(command):
                    if i in self.commands:
                        return f"Command not found. Did you mean '/{i}'?", YOUNEEDHELP, "spelling"
                raise InvalidCommandError(full_command, INVALIDMSG)
        else: 
            raise NoSlashError(full_command, NOSLASHMSG)
        
        return title, return_msg, type

    def displayTasks(self, user, status, time, timecheck=False):
        string = ""
        for i in range(len(self.tasks[user])):
            if self.tasks[user][i].status == status:
                if timecheck:
                    yesterday = time - timedelta(days=1)
                    if self.tasks[user][i].completed_on >= yesterday: 
                        string += f"Task {i}: {self.tasks[user][i]} \n\n"
                else:
                    string += f"Task {i}: {self.tasks[user][i]} \n\n"
        if string == "":
            string = "No tasks stored."           
        return string
    
    def displayStandUpHelper(self, user, utc, timecheck=False): 
        complete = self.displayTasks(user, COMPLETE, utc, timecheck)
        incomplete = self.displayTasks(user, INPROGRESS, utc)
        return f"Completed Tasks: \n\n {complete} \n\n Incomplete Tasks:\n\n {incomplete}"

    def edits1(self,word):
        alphabet = string.ascii_lowercase
        splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes    = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
        inserts    = [a + c + b     for a, b in splits for c in alphabet]
        return set(deletes + transposes + replaces + inserts)
    
    def edits2(self, word): 
        """All edits that are two edits away from `word`."""
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

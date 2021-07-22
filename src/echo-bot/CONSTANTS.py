""" Bot Commands """

ADD_TODO = "/todo"
DELETE_TODO = "/completed"

HELPERMSG = "Here are the following commands: \n\n\n\n" \
            "'/standup' prompts StandUpBuddy and helps prepare you for your next standup meeting. \n\n" \
            "'/todo [description] [priority=None]'creates a new task. \n\n" \
            "'/complete [task]' moves task from im progress list to completed list. \n\n"\
            "'/show' displays all of your incomplete tasks. \n\n "\
            "'/show completed' displays all of your completed tasks. \n\n "\
            "'/show all' displays all of your tasks. \n\n" \
            "'/remove [task]' deletes the task that you specify. \n\n "\
            "'/clear' deletes all tasks. \n\n" \
            "'/edit [task]' marks a task active for editing. By default, the most recently added task is active for editing. \n\n\n\n" \
            "After using '/edit [task]' use the following to change task attributes:\n\n" \
            "    *'/priority [priority]' \n\n" \
            "    *'/description [description]'\n\n" \
            "    *'/status [status]'\n\n\n\n "\
            "Priority is a number from 1-4, with 1 being the highest priority. \n\n" \
            "Status can be either 'in progress' or 'complete'. \n\n"

NOSLASHMSG = "Commands must begin with the '/' character."
INVALIDMSG = " is not a valid command. See '/help'."
YOUNEEDHELP = "You can use ‘/help’ to see all possible commands."

WELCOMEMSG = "If you're looking for help using StandUpBuddy,"\
          "see a list of available commands, use '/help'! \n\n"\
          "Please tell me when your stand up meetings are "\
          "by selecting one of the following, or simply tell me "\
          "in 24hr time, in the format 'HH-MM'"         
### STATUS CONSTANTS ###
INPROGRESS = "in progress"
BLOCKED = "blocked"
COMPLETE = "complete"

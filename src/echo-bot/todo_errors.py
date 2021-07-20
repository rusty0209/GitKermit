

class InvalidCommandError(Exception):

    def __init__(self, command, message):
        self.command = command
        self.message = message
    


class NoSlashError(Exception):

    def __init__(self, command, message):
        self.command = command
        self.message = message
    

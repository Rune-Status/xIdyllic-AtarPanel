import os as system
import shlex
import subprocess as subproc # If you're going to use check_call, don't use stdour or stderr. Deadlocking threads is a no-go.
from controllers.files import Files

"""It's important to make sure we don't leave vulnerabilites here. Using system/os.stat
will allow us to return bit permissions for a file. We don't want no SUID exploits."""

class Commands:

    invalid_commands = ['rm', 'rf', 'chmod'] # Input sanitization
    files = Files

    def __init__(self):
        pass

    def get_command(self):
        command_line = input()
        if command_line in self.invalid_commands:
            print("Command not allowed.") # This will eventually be logged, not output.
            exit()
        else:
            args = shlex.split(command_line)
            print(subproc.Popen(args, shell=True))

    def get_permissions(self, file):
        file_permission = None
        system.stat(file)

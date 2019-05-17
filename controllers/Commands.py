import os as system
import shlex
import subprocess as subproc # If you're going to use check_call, don't use stdour or stderr. Deadlocking threads is a no-go.
from controllers import Files

"""It's important to make sure we don't leave vulnerabilites here. Using system/os.stat
will allow us to return bit permissions for a file. We don't want no SUID exploits."""

class Commands:

    invalid_commands = {'rm', 'rf', 'chmod'} # Input sanitization
    command_line = input()
    files = Files.Files

    def __init__(self):
        pass

    def get_command(self, command):
        arguments = shlex.split(self.command_line)
        if self.invalid_commands in arguments:
            exit()

    def get_permissions(self):
        system.stat(self.files.getFile())
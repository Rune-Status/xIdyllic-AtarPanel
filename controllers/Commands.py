import os
import shlex
import subprocess # If you're going to use check_call, don't use stdour or stderr. Deadlocking threads is a no-go.
from controllers.files import Files

"""It's important to make sure we don't leave vulnerabilites here. Using system/os.stat
will allow us to return bit permissions for a file. We don't want no SUID exploits."""

class Commands:

    def __init__(self):
        self.files = Files
        self.subproc = subprocess
        self.system = os
        self.users = self.system.system('cut -d: -f1 /etc/passwd')
        self.invalid_commands = ['rm', 'rf', 'chmod']  # Input sanitization

    def get_command(self, command=None):
        if command:
            if self.check_command(command):
                self.subproc.Popen(command, shell=True)
            else:
                return False
        if not command:
            command_line = input()
            if self.check_command(command_line):
                self.subproc.Popen(command_line, shell=True)
            else:
                return False

    def get_permissions(self, file):
        file_permission = None
        file_stats = self.system.stat(file) # Allows deeper checks rather than os.getuid, etc.


    def get_user(self, user=None):
        if user:
            self.subproc.check_output()

    def check_command(self, cmd=None):
        if cmd in self.invalid_commands:
            print("Command not allowed!")
            exit()
            return False
        else:
            return True

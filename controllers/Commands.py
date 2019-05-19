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
        self.invalid_commands = ['rm', 'rf', 'chmod']  # Input sanitization
        self.users = shlex.split('cut -d: -f1 /etc/passwd')

    def get_command(self, command=None):
        if command:
            if self.check_command(command):
                self.subproc.Popen(command, shell=True, stderr=self.subproc.PIPE, stdout=self.subproc.PIPE)
            else:
                return False
        if not command:
            command_line = input()
            if self.check_command(command_line):
                self.subproc.Popen(command_line, shell=True, stderr=self.subproc.PIPE, stdout=self.subproc.PIPE)
            else:
                return False

    def get_permissions(self, file):
        file_permission = None
        file_stats = self.system.stat(file) # Allows deeper checks rather than os.getuid, etc.


    def get_users(self, user=None):
        if user:
            user_command_output = self.subproc.Popen(self.users, stderr=self.subproc.PIPE, stdout=self.subproc.PIPE)
            if user in user_command_output.communicate()[0].decode('utf-8'):
                print('User Exists')
                return True
        if not user:
            self.subproc.Popen(self.users)

    def check_command(self, cmd=None):
        if cmd in self.invalid_commands:
            print("Command not allowed!")
            exit()
            return False
        else:
            return True

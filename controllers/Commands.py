import os
import shlex
import subprocess # If you're going to use check_call, don't use stdour or stderr. Deadlocking threads is a no-go.
import sys
from controllers import Files

"""It's important to make sure we don't leave vulnerabilites here. Using system/os.stat
will allow us to return bit permissions for a file. We don't want no SUID exploits."""

class Commands:

    def __init__(self):
        self.files = Files.Files
        self.subproc = subprocess
        self.system = os
        self.invalid_commands = ['rm', 'rf', 'chmod']  # Input sanitization
        self.users = shlex.split('cut -d: -f1 /etc/passwd')
        self.permission_index = {
            0: 'st_mode',
            1: 'st_ino',
            2: 'st_dev',
            3: 'st_nlink',
            4: 'st_uid',
            5: 'st_gid',
            6: 'st_size',
            7: 'st_atime',
            8: 'st_mtime',
            9: 'st_ctime'
        }
        self.bit_list = []


    def clear_screen(self):
        self.subproc.call('clear')
        return True

    def grep_file(self, file, item_to_grep):
        if file and item_to_grep:
            self.subproc.check_call(['grep', '-a', file, item_to_grep])

    def get_permission_bits(self, file):
        file_ids = self.system.stat(file)
        try:
            for index, ids in enumerate(file_ids):
                try:
                    self.bit_list = [index, ids, self.permission_index[index]]
                    print(self.bit_list)
                except (IndexError, OverflowError, Exception) as err:
                    print(err)
        except Exception as err:
            print(err)

    def get_users(self, user=None):
        if user:
            user_command_output = self.subproc.Popen(self.users, stderr=self.subproc.PIPE, stdout=self.subproc.PIPE)
            if user in user_command_output.communicate()[0].decode('utf-8'):
                print('User Exists')
                return True
        if not user:
            self.subproc.Popen(self.users)
            exit()

    def check_command(self, cmd=None):
        if cmd in self.invalid_commands:
            print("Command not allowed!")
            exit()
            return False
        else:
            return True

    def flush_std_buffers(self, stdin=False, stdout=False):
        stdin = sys.__stdin__
        stdout = sys.__stdout__

        try:
            if stdin:
                stdin.flush()
                print("STDIN buffers flushed.")
            if stdout:
                stdout.flush()
                print("STDOUT buffers flushed.")
            if stdout and stdin:
                stdin.flush()
                stdout.flush()
                print("STDIN and STDOUT buffers flushed.")
        except (SystemError, IOError) as err:
            print(err)


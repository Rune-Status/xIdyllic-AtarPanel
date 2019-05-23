from pathlib import Path
import shutil, subprocess

# This class will need to rely heavily on commands.py for checking permissions and such.

class Files:

    def __init__(self):
        self.subproc = subprocess
        self.path = None
        self.file_util = shutil
        self.path_util = Path
        self.log_paths = ['logs/']

    def get_file(self, file):
        try:
            if Path(file).is_file():
                print(file)
                return
        except (FileNotFoundError, PermissionError, OSError) as err:
            print(err)  # log this

    def get_dir(self, directory):
        try:
            if self.path_util().is_absolute():
                print(directory)
                return
        except (FileNotFoundError, PermissionError, OSError) as err:
            print(err)  # log this

    def copy_file(self, file, desination_path):
        try:
            self.file_util.copyfile(file, desination_path)
        except (PermissionError, OSError, FileNotFoundError) as err:
            print(err)

    def remove_file(self, file):
        try:
            self.path_util.unlink(file)
        except (PermissionError, OSError, FileNotFoundError) as err:
            print(err)

    def read_ip_file(self, file, user=None):
        if user:
            try:
                self.subproc.check_call(['grep', '-a', user, file])
            except (OSError, PermissionError, FileNotFoundError) as err:
                print(err)
        if not user:
            try:
                self.subproc.check_call(['tail', '-500', file])
            except (OSError, PermissionError, FileNotFoundError) as err:
                print(err)

    def read_log_file(self, path, user):
        if not path and user:
            pass
        if path and user:
            try:
                complete_path = path + user + '.txt'
                self.tail_file(complete_path)
            except (OSError, PermissionError, FileNotFoundError) as err:
                print(err)

    def compare_users(self, user1, user2):
        user1 = user1 + '.txt'
        user2 = user2 + '.txt'
        if self.path_util(self.log_paths[0] + user1).is_file():
            print(user1, ' exists')
            if self.path_util(self.log_paths[0] + user2).is_file():
                print(user2, ' exists')
                self.tail_file('-10', self.log_paths[0] + user1)
                self.tail_file('-10', self.log_paths[0] + user2)

    def tail_file(self, lines_to_tail, file):
        if int(lines_to_tail) < 0:
            self.subproc.check_call(['tail', str(lines_to_tail), file])
        if int(lines_to_tail) > 0:
            raise ValueError("Needs to be an argument, not just a number.")

    def backup_operation(self, directories):
        pass


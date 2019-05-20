from pathlib import Path
import shutil, subprocess

# This class will need to rely heavily on commands.py for checking permissions and such.

class Files:

    def __init__(self):
        self.subproc = subprocess
        self.path = None
        self.file_util = shutil
        self.path_util = Path

    def get_file(self, file):
        try:
            if Path(file).is_file():
                print(file)
                return
        except (FileNotFoundError, PermissionError, OSError) as err:
            print(err)  # log this

    def get_dir(self, directory):
        try:
            if Path(directory).is_absolute():
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
                for line in open(file, 'rt'):
                    line.rstrip()
                    self.subproc.check_call(['grep', '-a', user, file])
                    break
            except (OSError, PermissionError, FileNotFoundError) as err:
                print(err)
        if not user:
            try:
                for line in open(file, 'rt'):
                    line.rstrip()
                    self.subproc.check_call(['tail', '-500', file])
                    break
            except (OSError, PermissionError, FileNotFoundError) as err:
                print(err)

    def read_log_file(self, path, user):
        if not path and user:
            print("Missing arguments!")
            exit()
        if path and user:
            try:
                complete_path = path + user
                for line in open(complete_path, 'rt'):
                    line.rstrip()
                    self.subproc.check_call(['tail', '-200', complete_path])
                    break
            except (OSError, PermissionError, FileNotFoundError) as err:
                print(err)

    def backup_operation(self, directories):
        pass


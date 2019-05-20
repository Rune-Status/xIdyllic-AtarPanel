from pathlib import Path
import shutil, re, subprocess

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

    def read_file(self, file, grep_user=None):
        if grep_user:
            for line in open(file, 'rt'):
                line.rstrip()
                self.subproc.check_call(['/bin/grep', '-a', grep_user, file])
                break

    def backup_operation(self, directories):
        pass


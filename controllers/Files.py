from pathlib import Path
from controllers import commands
import shutil

# This class will need to rely heavily on commands.py for checking permissions and such.

class Files:

    def __init__(self):
        self.command_controller = commands
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

    def backup_operation(self, directories):
        pass


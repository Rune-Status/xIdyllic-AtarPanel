from pathlib import Path
import os
from controllers import commands


class Files:

    def __init__(self):
        self.command_controller = commands
        self.path = None

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

    def copy_file(self):
        pass

    def remove_file(self):
        pass

    def backup_file(self, files=None):
        pass
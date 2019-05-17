import os as system
import subprocess as subproc
from controllers import Files

"""It's important to make sure we don't leave vulnerabilites here. Using system/os.stat
will allow us to return bit permissions for a file. We don't want no SUID exploits."""

class Commands:

    files = Files.Files

    def __init__(self):
        pass

    def get_command(self):
        pass

    def get_permissions(self):
        system.stat(self.files.getFile())
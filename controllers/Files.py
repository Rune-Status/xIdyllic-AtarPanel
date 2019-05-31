from pathlib import Path
import shutil, subprocess
from controllers import Commands

# This class will need to rely heavily on commands.py for checking permissions and such.

class Files:

    def __init__(self):
        self.subproc = subprocess
        self.command_controller = Commands.Commands
        self.path = None
        self.file_util = shutil
        self.path_util = Path
        self.log_path = ['/home/game/server/data/playersaves/logs/']
        self.log_files = ['AddressLogs.txt', 'donationLogs.txt']
        self.log_dirs = ['commandlogs/',
                         'droplogs/',
                         'iplogs/',
                         'stakelogs/',
                         'chatlogs/',
                         'grandexchangelogs/',
                         'itempickuplogs/',
                         'pmlogs/',
                         'tradelogs/']

    def copy_file(self, source_file, destination_path):
        pass

    def remove_file(self, file):
        pass

    def read_address_log(self, user=None):
        if user:
            self.command_controller().grep_file(self.log_path[0] + self.log_files[0], user)

    def read_log_file(self, user, logtype):
        if user and logtype:
            for user in open(self.log_path[0] + logtype + user + '.txt', 'rt'):
                if logtype in self.log_dirs:
                    print(user, end='')

    def compare_users(self, logtype, user1, user2):
        for element in self.log_dirs:
            if logtype in element:
                self.command_controller().tail_file(self.log_path[0] + logtype + user1 + '.txt')
                print()
                self.command_controller().tail_file(self.log_path[0] + logtype + user2 + '.txt')
                break

    def backup_operation(self, directories):
        pass


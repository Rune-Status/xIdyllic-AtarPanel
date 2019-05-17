'import sys, getopt << will be needed to implement sys.argv[0] for verbose options and debugging.'
from controllers import Administration, Commands, Files

class Main:

    file_controller = Files.Files()
    command_controller = Commands.Commands()
    admin_controller = Administration.Administration()

    log_path = ''
    ataraxia_containers = {}
    arg_list = {}

    def main(self):
        self.file_controller.__init__()
        self.command_controller.__init__()
        self.admin_controller.__init__()

    def help(self):
        pass

if __name__ == "__main__":
    'self.main.sysargv[arg_list:]'
    pass
'import sys, getopt << will be needed to implement sys.argv[0] for verbose options and debugging.'
from controllers import administration, commands, files

class Main:

    file_controller = files.Files()
    command_controller = commands.Commands()
    admin_controller = administration.Administration()

    log_path = ''
    ataraxia_containers = {}
    arg_list = {}

    def __main__(self):
        pass

    def help(self):
        pass


if __name__ == '__main__':
    Main().__main__()

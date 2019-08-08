'import sys, getopt << will be needed to implement sys.argv[0] for verbose options and debugging.'
from controllers import Menu
from controllers import Commands
from controllers import Files
from controllers import Logging
import time


class Main:

    log_path = ''
    ataraxia_containers = {}
    arg_list = {}

    file_controller = Files.Files
    commands_controller = Commands.Commands
    log_controller = Logging.Logging
    administration = Menu.Menu

    if __name__ == '__main__':
        print("Initing commands controller")
        commands_controller().__init__()
        print("Initing log controller")
        log_controller().__init__()
        print("Initing file controller")
        file_controller().__init__()
        print("Initing Admin panel")
        administration().__init__()
        print("Starting Admin menu\n")
        administration().start_menu()

    def help(self):
        pass


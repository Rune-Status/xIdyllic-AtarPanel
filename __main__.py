'import sys, getopt << will be needed to implement sys.argv[0] for verbose options and debugging.'
from controllers.administration import Administration
from controllers.commands import Commands
from controllers.files import Files
from controllers.logging import Logging


class Main:

    log_path = ''
    ataraxia_containers = {}
    arg_list = {}

    file_controller = Files
    commands_controller = Commands
    log_controller = Logging
    administration = Administration

    if __name__ == '__main__':
        print("Initing commands controller")
        commands_controller().__init__()
        print("Initing log controller")
        log_controller().__init__()
        print("Initing file controller")
        file_controller().__init__()
        print("Initing Admin panel\n")
        administration().__init__()

    def help(self):
        pass


from controllers import Files
from controllers import Commands
from consolemenu import *
from consolemenu.prompt_utils import PromptUtils
import __main__

class Administration:

    def __init__(self):
        self.main_menu = [
            'Game Logs',
            'User Logs',
            'Server Control'
        ]
        self.game_log_menu = [
            'IP',
            'Drop',
            'PM',
            'Trade',
            'Chat',
            'Grand Exchange',
            'Item Pickup(s)',
            'Staking',
            'Commands',
            'Dontation',
            'Go Back'
        ]

        self.server_menu = [
            'Restart',
            'Shutdown',
            'Go back'
        ]

        self.target_user = None
        self.latest_update = 'fucking yes boy'
        self.file_controller = Files.Files
        self.command_controller = Commands.Commands
        self.menu = ConsoleMenu()
        self.prompt = PromptUtils(self.menu.screen)

    def start_main_menu(self):
        selection_main_menu = SelectionMenu.get_selection(self.main_menu, "Control Panel", "Latest development update: " + self.latest_update)
        if selection_main_menu == 0:
            if self.start_game_menu() == 0:
                user_to_search = self.get_input('Enter username of IP logs to view (lowercase): ')
                self.file_controller().read_log_file(str(user_to_search), self.file_controller().log_dirs[0])
                self.prompt.enter_to_continue('Press enter to go back to the previous menu')
            if self.start_game_menu() == 1:
                user_to_search = self.get_input('Enter username of drop logs to view (lowercase): ')
                self.file_controller().read_log_file(str(user_to_search), self.file_controller().log_dirs[1])

    def start_game_menu(self):
        selection_game_menu = SelectionMenu.get_selection(self.game_log_menu, "Select Game logs to view: ")
        return selection_game_menu

    def get_input(self, message):
        if message:
            user_input = self.prompt.input(message)
            input_result = getattr(user_input, 'input_string')
            return input_result
        if not message:
            print("get_input requires message parameter")
            exit()
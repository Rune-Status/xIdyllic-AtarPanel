from controllers import Files
from controllers import Commands
from consolemenu import *
from consolemenu.items import *
import __main__

class Administration:

    def __init__(self):
        self.main_menu = [
            'Game Logs',
            'User Logs',
            'Server Control'
        ]
        self.user_log_menu = {
            'IP',
            'Drop',
            'PM',
            'Trade',
            'Chat',
            'Donation',
            'Grand Exchange',
            'Item Pickup(s)',
            'Staking',
            'Commands',
            'Go Back'
        }

        self.server_menu = {
            'Restart',
            'Shutdown',
            'Go back'
        }

        self.target_user = None
        self.latest_update = 'fucking yes boy'
        self.file_controller = Files.Files
        self.command_controller = Commands.Commands
        self.menu = ConsoleMenu
        self.start_selection = SelectionMenu.get_selection(self.main_menu, "Control Panel", "Latest development update: " + self.latest_update)

    def start_menu(self):
        self.menu().show()



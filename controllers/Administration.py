from controllers import Files
from controllers import Commands

class Administration:

    def __init__(self):
        self.main_menu = {
            1: 'Game Logs',
            2: 'User Logs',
            3: 'Server Control'
        }
        self.user_log_menu = {
            1: 'IP Logs',
            2: 'Drop Logs',
            3: 'PM Logs',
            4: 'Trade Logs',
            5: 'Chat Logs',
            6: 'Donation Logs',
            7: 'GE Logs',
            8: 'Item Pickup Logs',
            9: 'Stake Logs'
        }
        self.server_menu = {
            1: 'Restart',
            2: 'Shutdown',
            3: 'Command Logs'
        }

        self.main_men = '[1] {}\n[2] {}\n[3] {}\n'.format(
            self.main_menu[1],
            self.main_menu[2],
            self.main_menu[3]
        )
        self.user_men = '[1] {}\n[2] {}\n[3] {}\n[4] {}\n[5] {}\n[6] {}\n[7] {}\n[8] {}\n[9] {}\n'.format(
            self.user_log_menu[1],
            self.user_log_menu[2],
            self.user_log_menu[3],
            self.user_log_menu[4],
            self.user_log_menu[5],
            self.user_log_menu[6],
            self.user_log_menu[7],
            self.user_log_menu[8],
            self.user_log_menu[9]
        )
        self.file_controller = Files.Files
        self.command_controller = Commands.Commands

    def start_menu(self):
        pass




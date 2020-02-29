from controllers import Files
from controllers import Commands


class Menu:

    def __init__(self):
        self.main_start = [
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
            'Donations',
            'Go Back'
        ]

        self.server_menu = [
            'Restart',
            'Shutdown',
            'Go back'
        ]

        self.menu_strings = [
            'Enter username to search: ',
            'Press enter to go back to the main menu.'
        ]

        self.target_user = None
        self.latest_commit = 'Menu has been rewritten.'
        self.file_controller = Files.Files
        self.command_controller = Commands.Commands

    def start_menu(self):
        self.command_controller().clear_screen()
        print("""
     _    _                            _           ____  ____  
    / \  | |_  __ _  _ __  __ _ __  __(_)  __ _   / ___||  _ \ 
   / _ \ | __|/ _` || '__|/ _` |\ \/ /| | / _` | | |    | |_) |
  / ___ \| |_| (_| || |  | (_| | >  < | || (_| | | |___ |  __/ 
 /_/   \_\\__|\__,_||_|   \__,_|/_/\_\|_| \__,_|  \____||_|    
\nLatest Update: {}""".format(self.latest_commit))
        self.set_menu('main')

        if self.get_user_choice() == 0:
            self.command_controller().clear_screen()
            self.set_menu('game')

    def get_user_choice(self):
        return int(input("\nSelect menu number: "))

    def get_player_log(self, logtype):
        self.file_controller().read_log_file(logtype, str(input("Enter the username you wish to search: ")))
        input('Press enter to go back when you are ready. This will refresh the current session.')
        self.set_menu('game')

    def get_staff_log(self):
        staff_rank = str(input("Please enter the rank of the staff member [support, mod, admin]: "))
        staff_user = str(input("Please enter the username of the staff member: "))
        self.file_controller().read_log_file(self.file_controller().log_dirs[8] + staff_rank
                                             + '/', staff_user)
        input('Press enter to go back when you are ready. This will refresh the current session.')
        self.set_menu('game')

    def set_menu(self, menu_select):
        if menu_select == 'game':
            self.print_menu_list(self.game_log_menu)
            self.game_menu()
        if menu_select == 'main':
            self.print_menu_list(self.main_start)
        if menu_select == 'server':
            self.print_menu_list(self.server_menu)

    def print_menu_list(self, menu_list):
        for menu_number, menu_type in enumerate(menu_list):
            print('[{}] - {}'.format(menu_number, menu_type))
            continue

    def game_menu(self):
        user_choice = self.get_user_choice()

        if user_choice == 0:
            self.get_player_log(self.file_controller().log_dirs[0])
        elif user_choice == 1:
            self.get_player_log(self.file_controller().log_dirs[1])
        elif user_choice == 2:
            self.get_player_log(self.file_controller().log_dirs[2])
        elif user_choice == 3:
            self.get_player_log(self.file_controller().log_dirs[3])
        elif user_choice == 4:
            self.get_player_log(self.file_controller().log_dirs[4])
        elif user_choice == 5:
            self.get_player_log(self.file_controller().log_dirs[5])
        elif user_choice == 6:
            self.get_player_log(self.file_controller().log_dirs[6])
        elif user_choice == 7:
            self.get_player_log(self.file_controller().log_dirs[7])
        elif user_choice == 8:
            self.get_staff_log()
        elif user_choice == 9:
            self.get_player_log(self.file_controller().log_dirs[9])
        elif user_choice == 10:
            self.start_menu()
        else:
            print("User could not be found or invalid input. Please try again.")
            self.game_menu()
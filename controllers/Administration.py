class Administration:

    def __init__(self):
        self.panel_args = {
            1: 'Game Logs',
            2: 'User Logs',
            3: 'Server Control',
            4: 'Restart',
            5: 'Shutdown',
        }
        self.panel_menu = '[1] {}\n[2] {}\n[3] {}\n'.format(self.panel_args[1], self.panel_args[2], self.panel_args[3])
        self.control_menu = '\n[1] {}\n[2] {}'.format(self.panel_args[4], self.panel_args[5])
        self.start_menu()

    def start_menu(self):
        print(self.panel_menu)
        try:
            user_input = int(input("Enter menu number: "))
            if user_input == 1:
                print("GAME LOGS")
                exit()
            if user_input == 2:
                print("USER LOGS")
                exit()
            if user_input == 3:
                print(self.control_menu)
                exit()
        except (KeyError, ValueError, OSError) as err:
            #logger.log(err)
            print("Invalid input! Try again.\n")
            self.start_menu()




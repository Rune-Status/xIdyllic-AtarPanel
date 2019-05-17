class Administration:

    panel_args = {
        1: 'Game Logs',
        2: 'User Logs',
        3: 'Server Control',
        4: 'Restart',
        5: 'Shutdown',
    }

    def start_panel(self, arg):
        return self.panel_args.get(arg, "Invalid input.")

    def menu(self, arg, print_menu=''):
        if (print_menu):
            return self.panel_args.get(arg, "Invalid input.")
        else:
            return self.panel_args.get(arg, "Invalid input.")

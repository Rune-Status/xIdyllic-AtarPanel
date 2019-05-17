class Administration:

    panel_args = {
        1: 'Game Logs',
        2: 'User Logs',
        3: 'Server Control',
        'Control_Menu': ['Restart', 'Shutdown']
    }

    control_menu = panel_args.get('Control_Menu', 'Invalid input.')

    def __init__(self):
        pass

    def start_panel(self, arg):
        return self.panel_args.get(arg, "Invalid input.")

    def menu(self, arg, control_menu=False):
        if control_menu:
            print(self.control_menu)
            if self.panel_args[arg] == 'Restart' or self.panel_args[arg] == 'Shutdown':
                return self.panel_args.get(self.control_menu)
            else:
                pass
        if not control_menu:

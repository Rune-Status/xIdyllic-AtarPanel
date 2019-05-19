import logging

class Logging:

    def __init__(self):
        self.log_directories = ['atar_panel_main.log']
        self.logger = logging
        self.logger.basicConfig(level=self.logger.DEBUG,
                                format='%(asctime)s %(levelname)-8s %(message)s',
                                datefmt='%d:%m:%y',
                                filename='logs/' + self.log_directories[0],
                                filemode='w+')

    def main_logging(self):
        pass

    def controller_logging(self):
        pass

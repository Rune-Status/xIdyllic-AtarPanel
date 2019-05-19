from pathlib import Path


class Files:

    def __init__(self):
        self.path = None

    def getFile(self, file):
        if Path(file).is_file():
            return file

    def getDir(self, directory):
        if Path(directory).is_absolute():
            return directory

# to import this class use that command -> from filenames import FilenameDir
import os

class FilenameDir:
    # This class will return the names of files within the specified folder
    def __init__(self,nameFolder):
        self.name = os.listdir('./' + nameFolder)
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        
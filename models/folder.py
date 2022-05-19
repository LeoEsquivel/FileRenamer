class Folder:
    
    def __init__(self, folder, filesName):
        self._folder = folder
        self._filesName = filesName

    #@property
    def get_folder(self):
        return self._folder

    #@property
    def get_filesName(self):
        return self._filesName

    
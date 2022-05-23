class Folder:
    
    def __init__(self, folder, filesName = []):
        self.__folder = folder
        self.__filesName = filesName

    def get_folder(self):
        return self.__folder

    def get_filesName(self):
        return self.__filesName

    
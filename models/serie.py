class Serie:

    def __init__(self, name, seasons):
        self.__name = name
        self.__seasons = seasons
        self.__chapters = []


    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getSeasons(self):
        return self.__seasons

    def setSeasons(self, new_seasons_list):
        self.__seasons = new_seasons_list

    def getChapters(self):
        return self.__chapters

    def setChapters(self, chapters_list):
        self.__chapters = chapters_list
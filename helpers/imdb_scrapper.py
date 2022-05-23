from bs4 import BeautifulSoup
import requests


class Scrapper:

    def __init__(self, url):
        self.__url = url
        self.__doc = BeautifulSoup( requests.get(url).text, "html.parser")
    
    
    def getPage(self):
        return self.__doc

    def getUrl(self):
        return self.__url


    def __setDoc(self, newPage):
        self.__doc = BeautifulSoup( requests.get(newPage).text, "html.parser" )


    # a, sc-89e7233a-0 jXxVEl
    def goToEpisodeGuide(self, html_tag="a", html_class="sc-89e7233a-0 jXxVEl"):
        episodeGuide = self.__doc.find(html_tag, class_= html_class )
        self.updateUrl_Doc(episodeGuide)
    

    def updateUrl_Doc(self, episodePage):
        char = (self.__url.find('?'))
        self.__url = self.__url[:char] + episodePage.get('href')
        self.__setDoc(self.__url)

    
    def getSeriesName(self):
        return self.__doc.find('h1').string


    def getSeasons(self):
        seasons = [str(x.text).strip() for x in self.__doc.find(id="bySeason").find_all('option')]
        return seasons


    def getSelectedSeasonLink(self, season):
        char = (self.__url.find('?'))
        self.__url = self.__url[:char] + "?season=" + season
        self.__setDoc(self.__url)

    
    def getChaptersName(self):
        chapters = self.__doc.find('div', class_="list detail eplist").find_all('div', class_="list_item")

        chapters_name = []
        for chapter in chapters:
            chapters_name.append(chapter.find('strong').text)

        return chapters_name            
        


from helpers import inquirer_menu
from helpers.imdb_scrapper import Scrapper
from helpers.renamer import Renamer
from models.folder import Folder
from models.serie import Serie

def main():
    while True:
        opt = inquirer_menu.MenuPrincipal()
        inquirer_menu.clearConsole()

        opt_selected = opt["select"]
        if '0.-' in opt_selected:    
            break
        elif '1.-' in opt_selected:
            opt = inquirer_menu.renameMenuOptions()
            
            opt_selected = opt["select"]
            if '1.-' in opt_selected:
                opt = inquirer_menu.imbd_MessageMenu()
                imbd_scrapper = Scrapper(opt.get('link'))

                seriesName = imbd_scrapper.getSeriesName()
                imbd_scrapper.goToEpisodeGuide()

                seasons = imbd_scrapper.getSeasons()

                serie = Serie(seriesName, seasons)

                opt = inquirer_menu.imdb_SeasonsMenu(serie.getSeasons())

                opt_selected = opt["season"]
                
                imbd_scrapper.getSelectedSeasonLink(opt_selected)
                serie.setChapters(imbd_scrapper.getChaptersName())

                opt = inquirer_menu.messageInputFolderName()

                data = Folder( opt["folder"] )

                renamer = Renamer()

                renamer.create_list(data.get_folder())
                renamer.create_list_new_names(serie.getChapters())
                renamer.change_filename(data.get_folder())

                inquirer_menu.pausa()

            

if __name__ ==  '__main__':
    
    main()


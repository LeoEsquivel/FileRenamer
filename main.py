from helpers import inquirer_menu
from helpers.renamer import Renamer
from models.folder import Folder

def main():
    while True:
        opt = inquirer_menu.MenuPrincipal()
        inquirer_menu.clearConsole()

        opt_selected = opt["select"]
        if '0.-' in opt_selected:    
            break
        elif '1.-' in opt_selected:
            opt = inquirer_menu.messagesInput()
            
            data = Folder( opt["carpeta"], opt["nombre_files"] )
            #data = Folder('D:\danie\Videos\OBS', 'Grabacion')

            renamer = Renamer()

            renamer.create_list(data.get_folder())

            renamer.create_list_new_names(data.get_filesName())

            renamer.change_filename(data.get_folder())

            inquirer_menu.pausa()
            



if __name__ ==  '__main__':
    
    main()


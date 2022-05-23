import os
import inquirer


menu_options = [
    inquirer.List('select', 
                    message='Seleccione una opción',
                    choices= [ '1.- Renombrar archivos', '0.- Salir',  ]    
                ),
]

rename_options = [
    inquirer.List('select', 
                    message='Seleccione una opción',
                    choices= [  
                                '1.- Agregar nombre desde IMDB',
                                '2.- Agregar solo nombre de la serie', 
                                '0.- Salir',  
                            ]    
                ),
]

def MenuPrincipal(): 
    answers = inquirer.prompt(menu_options)
    return answers

def renameMenuOptions():
    answer = inquirer.prompt(rename_options)
    return answer

def messagesInputManual():
    answers = [
        inquirer.Text(name="carpeta", message="Ingresa la locación de la carpeta"),
        inquirer.Text(name="nombre_files", message="Ingresa el nombre de la serie"),
    ]

    return inquirer.prompt(answers)

def messageInputFolderName():
    answer = [
        inquirer.Text(name="folder", message="Ubicación de la carpeta")
    ]

    return inquirer.prompt(answer)

def imbd_MessageMenu():
    answers = [
        inquirer.Text(name="link", message="Ingresa la pagina de IBDB de la serie"),
    ]

    return inquirer.prompt(answers)

def imdb_SeasonsMenu( seasons ):
    question = [
        inquirer.List('season',
                        message="Seleccione una temporada",
                        choices= seasons
                    )
    ]

    return inquirer.prompt(question)

def pausa():
    question = [
        inquirer.Text( name="enter", message="Presione ENTER para continuar." )
    ]

    inquirer.prompt(question)


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
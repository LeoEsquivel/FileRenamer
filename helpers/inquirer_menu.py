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
                    choices= [  '1.- Agregar nombre manual',
                                '2.- Agregar nombre desde IMDB', 
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

def messagesInput():
    answers = [
        inquirer.Text(name="carpeta", message="Ingresa la locación de la carpeta: "),
        inquirer.Text(name="nombre_files", message="Ingresa el nombre de la serie: "),
    ]

    return inquirer.prompt(answers)


def pausa():
    question = [
        inquirer.Text( name="enter", message="Presione ENTER para continuar." )
    ]

    inquirer.prompt(question)


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
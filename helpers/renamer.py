import os, time
from re import S
from progress.bar import ChargingBar

class Renamer:
    
    def __init__(self):
        self.__new_list = []
        self.__new_list_updated = []


    #Obtiene la lista de archivos dentro de la carpeta 
    def create_list(self, directorio):
        
        if os.path.exists(directorio):
            self.__new_list = os.listdir(directorio)
        else:
            print("El directorio no existe.")


    def getFolderFilesList(self):
        return self.__new_list


    def create_list_new_names(self, new_name):
        for i in range(len(self.__new_list)):
            new_n = self.new_name(self.__new_list[i], new_name[i], i)
            #new_n = self.newName(self._new_list[i], new_name, self._new_list[self._new_list.index('.'):], i)
            self.__new_list_updated.append(new_n)  


    def change_filename(self, directorio):
        size = len(self.__new_list_updated)
        bar = ChargingBar('Changing names', max=size)
        for i in range(size):
            os.rename((directorio+"/"+self.__new_list[i]), (directorio+"/"+self.__new_list_updated[i]))
            bar.next()
        bar.finish()



    newName = lambda currently_name, new_name, fileFormat, i: currently_name.replace(currently_name, '0'+str(i+1)+' - '+new_name+fileFormat) if (i+1) < 10 else currently_name.replace(currently_name, str(i+1)+' - '+new_name+fileFormat)

        
    def new_name(self, currently_name, new_name, i):
        fileFormat = currently_name[currently_name.index('.'):]
        if (i+1) < 10:
            return currently_name.replace(currently_name, '0'+str(i+1)+' - '+new_name+fileFormat)
        elif (i+1) >= 10:
            return currently_name.replace(currently_name, str(i+1)+' - '+new_name+fileFormat)

        
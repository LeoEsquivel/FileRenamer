import os, time
from progress.bar import ChargingBar

class Renamer:
    
    def __init__(self):
        self._new_list = []
        self._new_list_updated = []

    #Obtiene la lista de archivos dentro de la carpeta 
    # y cuandos archivos contiene.
    def create_list(self, directorio):
        
        if os.path.exists(directorio):
            self._new_list = os.listdir(directorio)
        else:
            print("El directorio no existe.")


    def create_list_new_names(self, new_name):
        for i in range(len(self._new_list)):
            new_n = self.new_name(self._new_list[i], new_name, i)
            #new_n = self.newName(self._new_list[i], new_name, self._new_list[self._new_list.index('.'):], i)
            self._new_list_updated.append(new_n)
  

    def change_filename(self, directorio):
        size = len(self._new_list_updated)
        bar = ChargingBar('Changing names', max=size)
        for i in range(size):
            os.rename((directorio+"/"+self._new_list[i]), (directorio+"/"+self._new_list_updated[i]))
            bar.next()

        
    def new_name(self, currently_name, new_name, i):
        fileFormat = currently_name[currently_name.index('.'):]
        if (i+1) < 10:
            return currently_name.replace(currently_name, new_name+' 0'+str(i+1)+fileFormat)
        elif (i+1) >= 10:
            return currently_name.replace(currently_name, new_name+' '+str(i+1)+fileFormat)

    newName = lambda self, currently_name, new_name, fileFormat, i: currently_name.replace(currently_name, new_name+' 0'+str(i+1)+fileFormat) if (i+1) < 10 else currently_name.replace(currently_name, new_name+' '+str(i+1)+fileFormat)
        
import json
import os


class Languajes():
    
    def __init__(self):
        self.__lanFile = "files/languajes.json"
        self.__lanDefault = "es"
    
    
    def load_languaje(self, languaje='es'):
        exist_lan = os.path.isfile(self.__lanFile)
        #print(exist_lan)
        if exist_lan == True:
            idiomas = open(self.__lanFile, 'r')
            diccionario = json.load(idiomas)
            idioma_seleccionado = diccionario[languaje]
            return idioma_seleccionado







# PRUEBAS DURANTE EL DESARROLLO
if __name__ == "__main__":
    
    lan = Languajes()
    test_lan = lan.load_languaje('es')
    print(test_lan)
    

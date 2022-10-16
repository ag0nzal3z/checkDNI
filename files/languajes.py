import json
import os


class Languajes():
    
    def __init__(self):
        self.__lanFile = "files/languajes.json"
        self.__lanConfDefault = "files/languaje"
    
    
    def load_languaje(self, languaje='es'):
        exist_lan = os.path.isfile(self.__lanFile)

        if exist_lan == True:
            idiomas = open(self.__lanFile, 'r')
            diccionario = json.load(idiomas)
            idioma_seleccionado = diccionario[languaje]
            idiomas.close()
            return idioma_seleccionado


    def load_default_lenguaje(self):
        exist_lan = os.path.isfile(self.__lanConfDefault)
        if exist_lan == False:
            file = open(self.__lanConfDefault, 'w')
            file.write("es")
        
        file = open(self.__lanConfDefault, 'r')
        content = file.readline()
        file.close()
        return content

    def save_select_languaje(self, selection):
        file = open(self.__lanConfDefault, 'w')
        file.write(selection)
        file.close()
        

# PRUEBAS DURANTE EL DESARROLLO
if __name__ == "__main__":
    
    lan = Languajes()
    test_lan = lan.load_languaje('es')
    print(test_lan)
    
    test_lan_defa = lan.load_default_lenguaje()
    print(test_lan_defa)
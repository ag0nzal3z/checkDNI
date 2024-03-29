# -*- coding: utf-8 -*-

import random
import os
from datetime import datetime

class DNI():
    
    def __init__(self):
        self.__secret_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        self.__secret_number = 23
        self.__lista_numeros_generados = [] 
    
    
    def check_input_data(self, number, word):
        """Verifica si los datos introducidos son correctos
        Parameters
        ----------
        number : str
            Numero de dni, solo digitos
        word : str
            Letra del dni, una letra
        Returns
        -------
        str
            Devuelve el tipo de error 
        """
        
        num_number_dni = 8
        word_number_dni = 1 
        if len(str(number)) != num_number_dni:
            return "La longitud no es correcta, debe de tener 8 digitos"

        if len(word) != word_number_dni or word.upper() not in self.__secret_dni:
            return "Has introducido mas de una letra o un caracter que no es una letra"
    
    
    def verification(self, number, word):
        control = int(number) % self.__secret_number
        letter = self.__secret_dni[control]
        if word.lower() == letter.lower():
            return "Correcto"
        else:
            return "Incorrecto"
        
        

    def wordGet(self, number, word):
        control = int(number) % self.__secret_number
        letter = self.__secret_dni[control]
        resultado = str(number) + letter
        return resultado

    # En desarrollo
    def numberGet(self, word, numDniGenerar):
        #lista_numeros_generados = []
        contador = 0
        #print("Antes del bucle")
        while contador < numDniGenerar:
            #print(contador)
            #contador = contador + 1
            #print(contador)
            numero_aleatorio = random.randrange(00000000, 99999999)    
            #print(numero_aleatorio)    
            #print(type(numero_aleatorio))
            if len(str(numero_aleatorio)) < 8:
                #print("Tiene 7 digitos, le agregamos 0 delante")
                numero_aleatorio = str(numero_aleatorio).rjust(8, '0')
                #print(numero_aleatorio)
            
            resto_numero_aleatorio = int(numero_aleatorio) % self.__secret_number
            #print(resto_numero_aleatorio)
            letra_numero_generado = self.__secret_dni[resto_numero_aleatorio]
            #print(letra_numero_generado)
            if letra_numero_generado.lower() == word:
                dni = str(numero_aleatorio)+letra_numero_generado.lower()
                if dni not in self.__lista_numeros_generados:
                    self.__lista_numeros_generados.append(dni)
                    contador = contador + 1
                
        return self.__lista_numeros_generados
    
    def generatorRandomDni(self, numDniGenerar):
        
        contador = 0
        while contador < numDniGenerar:
            numero_aleatorio = random.randrange(00000000, 99999999)
            
            if len(str(numero_aleatorio)) < 8:
                numero_aleatorio = str(numero_aleatorio).rjust(8, '0')

            resto_numero_aleatorio = int(numero_aleatorio) % self.__secret_number
            letra_numero_generado = self.__secret_dni[resto_numero_aleatorio]
            dni = str(numero_aleatorio)+letra_numero_generado.lower()
            if dni not in self.__lista_numeros_generados:
                self.__lista_numeros_generados.append(dni)
                contador = contador + 1
            
        return self.__lista_numeros_generados
    
    
    
class Logs():
    
    
    def __init__(self):
        self.__name_log = "cdni.log"
        #self.__timelog = datetime.now().isoformat(timespec='seconds')
    
    
    def create_file_log(self):
        now = datetime.now().isoformat(timespec='seconds')
        exist_log = os.path.isfile(self.__name_log)
        
        if exist_log == False:
            file = open(self.__name_log, "w")
            file.write(f"{now} ==> Inicio Archivo Log\n")
            file.close()
        elif exist_log == True:
            file = open(self.__name_log, "a")
            file.write(f"{now} ==> Inicio CheckDNI\n")
            file.close()


    def write_in_log(self, message):
        now = datetime.now().isoformat(timespec='seconds')
        file = open(self.__name_log, "a")
        file.write(f"{now} ==> {message}\n")
        file.close()
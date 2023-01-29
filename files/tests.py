# -*- coding: utf-8 -*-

from clases import DNI
from datetime import datetime
from languajes import Languajes






if __name__ == "__main__":
    # Test con DNI correcto
    numero = 11111111
    letra = "h"
    dni = DNI()
    estado = dni.check_input_data(numero, letra)
    resultado = dni.verification(numero, letra)
    print(resultado)
    
    
    # Test con DNI incorrecto
    numero = 11111135
    letra = "h"
    dni = DNI()
    estado = dni.check_input_data(numero, letra)
    resultado = dni.verification(numero, letra)
    print(resultado)
    
    
    # Test de obtencion de una letra que no corresponde con el numero,
    # por la letra que le corresponde a ese numero de dni
    numero = 11111111
    letra = "z"
    dni = DNI()
    estado = dni.check_input_data(numero, letra)
    resultado = dni.wordGet(numero, letra)
    conversion = dni.wordGet(numero, letra)
    print(conversion)
    
    # Test de obtencion de numeros de dni mediante la letra
    # se le pasa la letra del dni y el numero de dni que se quieren generar
    dni = DNI()
    dni_generados = dni.numberGet("h", 20)
    print(dni_generados)
    
    # Test de generacion de n numeros de dni validos
    dni = DNI()
    dni_aleatorios_generados = dni.generatorRandomDni(50)
    print(dni_aleatorios_generados)
    
    # Test de medidas de la pantalla en la que se ejecuta el programa
    import tkinter as tk
    pantalla_ordenador = tk.Tk()
    def medidas_monitor(r):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        print(f"Altura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
    medidas_monitor(pantalla_ordenador)
    
    
    # Test archivo log
    def create_file_log():
        name_log = "cdni.log"
        import os
        from datetime import datetime
        exist_log = os.path.isfile(name_log)
        print(exist_log)
        
        if exist_log == False:
            now = datetime.now().isoformat(timespec='seconds')
            file = open(name_log, "w")
            file.write(f"{now} ==> Inicio Archivo Log\n")
            file.close()
            print("Se ha creado el archivo")
        else:
            print("El archivo de log ya existe, no es necesario crearlo")
        
    create_file_log()
    
    # Test escritura mensajes en el log
    def write_in_log(message, name_log):
        now = datetime.now().isoformat(timespec='seconds')
        file = open(name_log, "a")
        file.write(f"{now} ==> {message}\n")
        file.close()
        
    write_in_log("Test de escritura en log", "cdni.log")


    # Test Languajes
    lan = Languajes()
    test_lan = lan.load_languaje('es')
    print(test_lan)
    print(test_lan['btn_validar'])
    
    # Test reinicio programa
    def program_restart_test() -> None:
        import os, sys
        #print(os.path.abspath(__file__))
        ruta_este_archivo = os.path.abspath(__file__)
        print(ruta_este_archivo)
        print(type(ruta_este_archivo))
        
        # Hay que poner un condicional para que si se usa linux sea '/' y si se usa windows sea '\\'
        lista_ruta_este_archivo = ruta_este_archivo.split(sep='\\')
        print(lista_ruta_este_archivo)
        print(type(lista_ruta_este_archivo))
        
        lista_ruta_main = lista_ruta_este_archivo[0:-2]
        print(lista_ruta_main)

        nombre_main = "checkDNI.py"
        
        lista_ruta_main.append(nombre_main)
        print(lista_ruta_main)
        # Hay que poner un condicional para que si se usa linux sea '/' y si se usa windows sea '\\\\'
        ruta_main = '\\\\'.join(lista_ruta_main)
        print(ruta_main)
        
        #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        #os.execl(sys.executable, ruta_main, *sys.argv)
        
        
        print("Se va a reiniciar el programa")
        print(f"os.execl(sys.executable, ruta_main, *sys.argv)")
        print("Programa reiniciado correctamente")
        
    program_restart_test()
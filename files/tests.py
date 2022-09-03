from clases import DNI







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
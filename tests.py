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
    
    
    
    
    # Test de generacion de n numeros de dni validos
    dni = DNI()
    numero_dni_generar = 100
    
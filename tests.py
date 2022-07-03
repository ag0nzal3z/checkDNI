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
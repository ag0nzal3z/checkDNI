
secret_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
secret_number = 23

class DNI():
    
    def check_input_data(self, number, word):
        num_number_dni = 8
        word_number_dni = 1 
        if len(str(number)) != num_number_dni:
            return "La longitud no es correcta, debe de tener 8 digitos"

        if len(word) != word_number_dni or word.upper() not in secret_dni:
            return "Has introducido mas de una letra o un caracter que no es una letra"
    
    
    def verification(self, number, word):
        control = int(number) % secret_number
        letter = secret_dni[control]
        if word.lower() == letter.lower():
            return "Correcto"
        else:
            return "Incorrecto"
        
        


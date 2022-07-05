

class DNI():
    
    def __init__(self):
        self.__secret_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        self.__secret_number = 23    
    
    
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
        
        

    def conversion(self, number, word):
        pass
    
    def generator(self, total):
        pass

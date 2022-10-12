#from tkinter import *
#from files.funciones import check_dni_windows, generar_dni_windows, menu_acerca_de, menu_contacto, menu_licencia
#from files.funciones import computer_os

from files.clases import Logs
logs = Logs()

from files.languajes import Languajes
lan = Languajes()


from files.funciones import main
    


if __name__ == "__main__":
    #select_lan = lan.load_languaje('es')
    lan_default = lan.load_default_lenguaje()
    #select_lan = lan.load_languaje('es')
    select_lan = lan.load_languaje(lan_default)
    main()
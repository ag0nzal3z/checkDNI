from tkinter import *
from files.funciones import check_dni_windows, generar_dni_windows, menu_acerca_de, menu_contacto, menu_licencia
from files.funciones import computer_os

from files.clases import Logs
logs = Logs()

from files.languajes import Languajes
lan = Languajes()



def main():
    # Ventana pantalla principal
    root = Tk()
    root.title("Check DNI")
    root.geometry("240x160")
    root.resizable(False, False)
    
    # Creacion archivo log
    logs.create_file_log()
    
    # OS en el que se ejecuta, para optimizar la multiplataforma
    if computer_os != "Linux":
        root.iconbitmap("files/images/icono_titulo.ico")
    else:
        root.iconbitmap("@files/images/icono_titulo.xbm")


    # Pantalla Principal
    frame_pantalla_principal = Frame()
    frame_pantalla_principal.pack()
    boton_check_dni = Button(frame_pantalla_principal, text=select_lan['btn_validar'], command=check_dni_windows)
    boton_check_dni.grid(row=2, column=2, padx=20, pady=25, columnspan=4)

    boton_generar_dni = Button(frame_pantalla_principal, text=select_lan['btn_generar'], command=generar_dni_windows)
    boton_generar_dni.grid(row=3, column=2, padx=20, pady=5, columnspan=4)

    # Menu
    menubar = Menu(root)
    menu_archivo = Menu(menubar, tearoff=0)
    menu_archivo.add_separator()
    menu_archivo.add_command(label=select_lan['men_arch'], command=root.quit)
    menubar.add_cascade(label=select_lan['men_bar_1'], menu=menu_archivo)

    menu_ayuda = Menu(menubar, tearoff=0)
    menu_ayuda.add_command(label=select_lan['men_ayu'], command=menu_acerca_de)
    menu_ayuda.add_command(label=select_lan['men_ayu_1'], command=menu_licencia)
    menu_ayuda.add_command(label=select_lan['men_ayu_2'], command='')  # En desarrollo
    menu_ayuda.add_separator()
    menu_ayuda.add_command(label=select_lan['men_ayu_3'], command=menu_contacto)
    menubar.add_cascade(label=select_lan['men_bar_2'], menu=menu_ayuda)

    root.config(menu=menubar)

    root.mainloop()
    


if __name__ == "__main__":
    #select_lan = lan.load_languaje('es')
    lan_default = lan.load_default_lenguaje()
    #select_lan = lan.load_languaje('es')
    select_lan = lan.load_languaje(lan_default)
    main()
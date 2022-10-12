from tkinter import *
from files.funciones import check_dni_windows, generar_dni_windows, menu_acerca_de, menu_contacto, menu_licencia
from files.funciones import computer_os

from files.clases import Logs
logs = Logs()

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
    boton_check_dni = Button(frame_pantalla_principal, text="Validar DNI", command=check_dni_windows)
    boton_check_dni.grid(row=2, column=2, padx=20, pady=25, columnspan=4)

    boton_generar_dni = Button(frame_pantalla_principal, text="Generar DNI", command=generar_dni_windows)
    boton_generar_dni.grid(row=3, column=2, padx=20, pady=5, columnspan=4)

    # Menu
    menubar = Menu(root)
    menu_archivo = Menu(menubar, tearoff=0)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Archivo", menu=menu_archivo)

    menu_ayuda = Menu(menubar, tearoff=0)
    menu_ayuda.add_command(label="Acerca de checkDNI", command=menu_acerca_de)
    menu_ayuda.add_command(label="Licencia", command=menu_licencia)
    menu_ayuda.add_separator()
    menu_ayuda.add_command(label="Contacto", command=menu_contacto)
    menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

    root.config(menu=menubar)

    root.mainloop()
    


if __name__ == "__main__":
    main()
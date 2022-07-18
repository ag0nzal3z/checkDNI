from tkinter import *
#from funciones import check_dni_windows
from clases import DNI
from tkinter import messagebox
#from tkinter import ttk
from funciones import checker, check_dni_windows

root = Tk()
root.title("Check DNI")
root.geometry("240x160")
root.resizable(False, False)
root.iconbitmap("files/icono_titulo.ico")




# Pantalla Principal
frame_pantalla_principal = Frame()
frame_pantalla_principal.pack()
boton_check_dni = Button(frame_pantalla_principal, text="Validar DNI", command=check_dni_windows)
boton_check_dni.grid(row=2, column=2, padx=20, pady=25, columnspan=4)

boton_generar_dni = Button(frame_pantalla_principal, text="Generar DNI", command="")
boton_generar_dni.grid(row=3, column=2, padx=20, pady=5, columnspan=4)










root.mainloop()
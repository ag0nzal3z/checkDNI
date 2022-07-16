from tkinter import *
#from funciones import *



root = Tk()
root.title("Check DNI")
root.geometry("240x160")
root.resizable(False, False)
root.iconbitmap("files/icono_titulo.ico")



def check_dni_windows():
    window = Toplevel()
    window.title("Validar DNI")
    window.iconbitmap("files/icono_titulo.ico")
    window.geometry("640x420")
    window.resizable(False, False)





# Pantalla Principal
frame_pantalla_principal = Frame()
frame_pantalla_principal.pack()
boton_check_dni = Button(frame_pantalla_principal, text="Validar DNI", command=check_dni_windows)
boton_check_dni.grid(row=2, column=2, padx=20, pady=25, columnspan=4)

boton_generar_dni = Button(frame_pantalla_principal, text="Generar DNI", command="")
boton_generar_dni.grid(row=3, column=2, padx=20, pady=5, columnspan=4)



# Pantalla Validar DNI












root.mainloop()
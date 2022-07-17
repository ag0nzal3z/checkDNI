from tkinter import *
#from funciones import check_dni_windows



root = Tk()
root.title("Check DNI")
root.geometry("240x160")
root.resizable(False, False)
root.iconbitmap("files/icono_titulo.ico")



def check_dni_windows():
    window = Toplevel()
    window.title("Validar DNI")
    window.iconbitmap("files/icono_titulo.ico")
    window.geometry("230x160")
    window.resizable(False, False)
    
    
    mensaje1 = Label(window, text="Introduce el DNI: ")
    mensaje1.grid(row=0, padx=5, pady=5)

    entrada_dni = Entry(window, width=35)
    entrada_dni.grid(row=1, padx=5, pady=5)

    boton_validar = Button(window, text="VERIFICAR")
    boton_validar.grid(row=4, padx=20, pady=25)




# Pantalla Principal
frame_pantalla_principal = Frame()
frame_pantalla_principal.pack()
boton_check_dni = Button(frame_pantalla_principal, text="Validar DNI", command=check_dni_windows)
boton_check_dni.grid(row=2, column=2, padx=20, pady=25, columnspan=4)

boton_generar_dni = Button(frame_pantalla_principal, text="Generar DNI", command="")
boton_generar_dni.grid(row=3, column=2, padx=20, pady=5, columnspan=4)










root.mainloop()
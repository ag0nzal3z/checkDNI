from tkinter import *
from clases import DNI
from tkinter import messagebox


def check_dni_windows():
    window = Toplevel()
    window.title("Validar DNI")
    window.iconbitmap("files/icono_titulo.ico")
    window.geometry("230x160")
    window.resizable(False, False)
    window.grab_set()
    
    mensaje1 = Label(window, text="Introduce el DNI: ")
    mensaje1.grid(row=0, padx=5, pady=5)

    entrada_dni = Entry(window, width=35)
    entrada_dni.grid(row=1, padx=5, pady=5)

    boton_validar = Button(window, text="VERIFICAR", command= lambda: checker(entrada_dni.get()) )
    boton_validar.grid(row=4, padx=20, pady=25)
    window.mainloop()
    
    
    
def checker(num):
    dni = DNI()
    numero = num
    num = num[0:8]
    lett = numero[-1]
    check = dni.check_input_data(num, lett)
    state = dni.verification(num, lett)
    messagebox.showinfo(message=state, title="Estado DNI")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# https://programacionfacil.org/cursos/tkinter/capitulo_15_nuevas_ventanas_con_toplevel.html
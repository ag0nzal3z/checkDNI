from tkinter import *
#from funciones import check_dni_windows
from clases import DNI
from tkinter import messagebox
#from tkinter import ttk

root = Tk()
root.title("Check DNI")
root.geometry("240x160")
root.resizable(False, False)
root.iconbitmap("files/icono_titulo.ico")



def checker(num):
    #messagebox.showinfo(message=num, title="Tests")
    #print(num)
    dni = DNI()
    numero = num
    num = num[0:8]
    lett = numero[-1]
    #print(num)
    #print(lett)
    check = dni.check_input_data(num, lett)
    state = dni.verification(num, lett)
    print(state)
    messagebox.showinfo(message=state, title="Estado DNI")
    #return state

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
    
    salida = Label(window, text ="Esto es una prueba"  )
    salida.grid(row=5)
    
    
    
    
    window.mainloop()


# Pantalla Principal
frame_pantalla_principal = Frame()
frame_pantalla_principal.pack()
boton_check_dni = Button(frame_pantalla_principal, text="Validar DNI", command=check_dni_windows)
boton_check_dni.grid(row=2, column=2, padx=20, pady=25, columnspan=4)

boton_generar_dni = Button(frame_pantalla_principal, text="Generar DNI", command="")
boton_generar_dni.grid(row=3, column=2, padx=20, pady=5, columnspan=4)










root.mainloop()
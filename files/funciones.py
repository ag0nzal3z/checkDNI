from tkinter import *
from files.clases import DNI
from tkinter import messagebox
from tkinter import filedialog


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
    
def generar_dni_windows():
    window = Toplevel()
    window.title("Generar DNI")
    window.iconbitmap("files/icono_titulo.ico")
    window.geometry("180x160")
    window.resizable(False, False)
    window.grab_set()
    
    mensaje1 = Label(window, text="Numero DNIs generar: ")
    mensaje1.grid(row=0, column=1, padx=5, pady=5)
    
    numero_dni_generar = Entry(window, width=10, justify=CENTER)
    numero_dni_generar.grid(row=1, column=1, padx=5, pady=5)
    
    boton_generar = Button(window, text="GENERAR", command= lambda: generar(numero_dni_generar.get()) )
    boton_generar.grid(row=2, column=1, padx=20, pady=10)
    
    boton_generar_en_archivo = Button(window, text="GENERAR EN ARCHIVO", command= lambda: generar_en_archivo(numero_dni_generar.get()) )
    boton_generar_en_archivo.grid(row=3, column=1, padx=20, pady=5)
    
    window.mainloop()

    
def checker(num):
    dni = DNI()
    numero = num
    num = num[0:8]
    lett = numero[-1]
    check = dni.check_input_data(num, lett)
    state = dni.verification(num, lett)
    messagebox.showinfo(message=state, title="Estado DNI")
    
    
    
def generar(numero):
    dni = DNI()
    dni_generados = dni.generatorRandomDni(int(numero))
    messagebox.showinfo(message=dni_generados, title="DNI Generados")
    

def generar_en_archivo(numero):
    dni = DNI()
    fichero = filedialog.asksaveasfile(
        title="Guardar un fichero", mode='w', defaultextension=".txt")
    dni_generados = dni.generatorRandomDni(int(numero))
    #proceso = messagebox.showinfo(message="Se esta generado el archivo")
    #proceso
    fichero.write(str(dni_generados))
    fichero.close()

def menu_acerca_de():
    mensaje_acerca_de = """
    
    Este programa ha sido programado con fines educativos
    
    Se ha creado usando:
    
        * Python 3.10.2
    
    No se han utilizado librerias de terceros externas a la instalacion de Python
    
    """
    messagebox.showinfo(message=mensaje_acerca_de, title="Acerca de checkDNI")


def menu_licencia():
    pass

def menu_contacto():
    mensaje_contacto = """
    Autor: Alberto González
    Email: Bertito@protonmail.com
    Github: ag0nzal3z
    """
    messagebox.showinfo(message=mensaje_contacto, title="Contacto")
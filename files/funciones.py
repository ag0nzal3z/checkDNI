from tkinter import *
from files.clases import DNI, Logs
from tkinter import messagebox
from tkinter import filedialog
import platform
computer_os = platform.system()
logs = Logs()

def check_dni_windows():
    window = Toplevel()
    window.title("Validar DNI")
    if computer_os != "Linux":
        window.iconbitmap("files/icono_titulo.ico")
    else:
        window.iconbitmap("@files/icono_titulo.xbm")
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
    if computer_os != "Linux":
        window.iconbitmap("files/icono_titulo.ico")
    else:
        window.iconbitmap("@files/icono_titulo.xbm")
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
    logs.write_in_log("Validacion DNI")
    dni = DNI()
    numero = num
    num = num[0:8]
    lett = numero[-1]
    check = dni.check_input_data(num, lett)
    state = dni.verification(num, lett)
    logs.write_in_log(f"DNI {state}")
    if state == "Correcto":
        messagebox.showinfo(message=state, title="Estado DNI")
    elif state == "Incorrecto":
        messagebox.showerror(message=state, title="Estado DNI")


def generar(numero):
    dni = DNI()
    if int(numero) > 4000:
        messagebox.showerror(message="El numero de DNIs a generar no puede ser superior a 4000", title="ERROR Generacion DNIs")
    else:
        dni_generados = dni.generatorRandomDni(int(numero))
        messagebox.showinfo(message=dni_generados, title="DNI Generados")
    

def generar_en_archivo(numero):
    dni = DNI()
    fichero = filedialog.asksaveasfile(
        title="Guardar un fichero", mode='w', defaultextension=".txt")
    dni_generados = dni.generatorRandomDni(int(numero))
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
    licencia = """
    
    https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
    
    https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.es
    
    """
    window = Toplevel()
    window.title("Licencia")
    window.geometry("470x200")
    imagen = PhotoImage(file="files/licencia.png")
    fondo = Label(window, image=imagen).place(x=0, y=0)
    window.mainloop()

def menu_contacto():
    mensaje_contacto = """
    Autor: Alberto González
    Email: Bertito@protonmail.com
    Github: ag0nzal3z
    """
    messagebox.showinfo(message=mensaje_contacto, title="Contacto")
    

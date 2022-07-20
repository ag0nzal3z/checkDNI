import PySimpleGUI as sg
from files.clases import DNI

layout = [  [sg.Text("Numero de DNI")],
            [sg.Input()],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Validar'), sg.Button('Salir')]]



window = sg.Window('checkDNI', layout)


while True:
    event, values = window.read()
    
    dato = values[0]
    #print(dato[0:8], dato[-1])
    
    dni = DNI()
    
    estado = dni.check_input_data(dato[0:8], dato[-1])
    
    #if estado != "OK":
    #    exit()
    
    resultado = dni.verification(int(dato[0:8]), dato[-1])
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    
    #print('El numero de DNI introducido es: ', values[0])
    window['-OUTPUT-'].update('El DNI introducido es: ' + resultado)



window.close()

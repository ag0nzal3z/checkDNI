# Programa validador de DNI para la linea de comandos
# -*- coding: utf-8 -*-

from files.clases import DNI
import argparse





















TODO #PONER LOS ARGUMENTOS NECESARIOS

if __name__ == "__main__":

    parser = argparse.ArgumentParser(

        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('''\
                    Uso de main.py
            --------------------------------
            Utiliza -s ruta del archivo (Por defecto la ruta donde se ejecuta el programa)
            Utiliza -d destino del archivo (Por defecto la ruta donde se ejecuta el programa)
            Utiliza -t tipo de conversion (Por defecto json)
            Utiliza -a archivo que contiene las rutas de origen (Cada linea tiene que ser una ruta)
            Ejemplo: python3 main.py -s /home/agonzalez/test.yml -d /var/test.json
            Ejemplo: python main.py -s /home/agonzalez/test.yml -d /var/test.json
            '''))

    parser.add_argument("-s",
        "--source",
        help="Ruta del archivo origen",
    )
    parser.add_argument(
        "-d",
        "--destination",
        help="Ruta destino del archivo",
    )
    parser.add_argument("-t",
        "--type",
        help="Tipo de conversion: 'json' o 'yaml' ",
    )
    parser.add_argument("-f",
        "--file",
        help="Leer origen el origen desde archivo, cada linea es una ruta",
    )



    args = parser.parse_args()


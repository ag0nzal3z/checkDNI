from files.languajes import Languajes
lan = Languajes()


from files.funciones import main
    


if __name__ == "__main__":
    #select_lan = lan.load_languaje('es')
    lan_default = lan.load_default_lenguaje()
    #select_lan = lan.load_languaje('es')
    select_lan = lan.load_languaje(lan_default)
    main()

menu = ["1. Registrar Automovil","2. Registro Mantenimiento","3. Consultar Automovil","4. Salir"]
autos = []
autosDet = []
campos = ["Patente: ","Marca: ","Modelo: ","Año Fabricación:: ","Tipo Vehículo: "]

activo = 0
while activo == 0:
    
    print("Bienvenido a la Serviteca ServiExpress")
    print("Para continuar debe seleccionar alguna de las siguientes opciones:")
    for a in menu:
        print(a)
    try:
        seleccion = int(input(""))
        if seleccion >0 and seleccion <5:
            if seleccion == 1: 
                autosDet.clear()
                print("------------------------------------------------------------------")
                print("Usted ha solicitado Registrar un automovil")
                print("Se le solicitarán algunos datos")
                revisor = 0
                while revisor == 0:
                    print("Ingrese la patente del Vehículo (debe contener sólo 6 carácteres)")
                    patente = str(input(""))

                    if len(patente) == 6:
                        baseNum = ["1","2","3","4","5","6","7","8","9","0"]
                        forma = -1
                        try:
                            numeros = int(patente[-4:])
                            letras = str(patente[0:2])
                            malo = 0
                            for b in letras:
                                if b in baseNum:
                                    malo = 1
                            if malo == 0:
                                forma = 1
                        except:
                            forma = 0
                        if forma < 1:
                            try:
                                numeros2 = int(patente[-2:])
                                letras2 = patente[0:4]
                                malo = 0
                                for c in letras2:
                                    if c in baseNum:
                                        malo = 1
                                if malo == 0:
                                    forma = 2
                            except:
                                forma = 0
                        
                        if forma > 0:
                            autosDet.append(patente)
                            revisor = 1
                        else:
                            print("La Patente no tiene un formato correcto")
                    else:
                        print("La Patente no tiene un formato correcto")
                revisor = 0
                while revisor == 0:
                    print("Ingrese la marca del vehículo")
                    marca = str(input(""))
                    if marca != "":
                        autosDet.append(marca)
                        revisor = 1
                    else:
                        print("Debe ingresar algún dato")
                revisor = 0
                while revisor == 0:
                    print("Ingrese el modelo del vehículo")
                    modelo = str(input(""))
                    if modelo != "":
                        autosDet.append(modelo)
                        revisor = 1
                    else:
                        print("Debe ingresar algún dato")
                revisor = 0
                while revisor == 0:
                    try:
                        print("Ingrese el año del vehículo")
                        año = int(input("")) 
                        if año >= 1900 and año <= 2021:
                            autosDet.append(año)
                            revisor = 1
                        else:
                            print("Debe ingresar un numero entre 1900 y 2021")      
                    except:
                        print("Dato mal ingresado")
                revisor = 0
                while revisor == 0:
                    print("Ingrese el tipo de vehículo dependiendo si es: bencina, diesel, eléctrico, híbrido, deberá ingresar los carácteres b, d, e o h")
                    tipo = str(input("")) 
                    ModTipo = ["b","d","e","h"]
                    if tipo.lower() in ModTipo:
                        autosDet.append(tipo)
                        revisor = 1
                    else:
                        print("Debe ingresar sólo uno de los siguientes carácteres: b, d, e, h")  
                autos.append(autosDet)
                print("Vehículo registrado")
            if seleccion == 2:
                if len(autos) == 0:
                    print("No hay ningún vehiculo registrado, antes debe acudir a la opción 1")
                else:
                    print("Ingrese la patente del vehículo a consultar")
                    consulta = str(input(""))
                    encontrado = -1
                    for busca in range(len(autos)):
                        print("buscando")
                        if consulta == autos[busca][0]:
                            encontrado = busca 
                    if encontrado >= 0:
                        print("El Vehículo patente ",consulta," fue encontrado")
                        print("Ingrese la fecha de mantenimiento para respaldo de la base:")
                        autos[encontrado].append(input(""))
                        campos.append("Fecha mantenimiento: ")
                        print("Ingrese las observaciones al mantenimiento:")
                        autos[encontrado].append(input(""))
                        campos.append("Observaciones mantenimiento: ")
                        print("Información registrada")
                    else:
                        print("No existe el vehículo en nuestros registros")
            if seleccion == 3:
                if len(autos) == 0:
                    print("No hay ningún vehiculo registrado, antes debe acudir a la opción 1")
                else:
                    print("Ingrese la patente del vehículo a consultar")
                    consulta = str(input(""))
                    encontrado = -1
                    for busca in range(len(autos)):
                        if consulta == autos[busca][0]:
                            encontrado = busca 
                    if encontrado >= 0:
                        print("**********************************************")
                        for muestra in range(len(autos[encontrado])):
                            print(campos[muestra],autos[encontrado][muestra])
                        print("**********************************************")
                    else:
                        print("No existe el vehículo en nuestros registros")
            if seleccion == 4:
                print("Cerrando sesión")
                activo = 1
            input("Presione enter para continuar")
            print("-----------------------------------------------------------------------")
        else:
            print("Ingrese un número del 1 al 4")

    except:
        print("Ingrese solo dígitos")

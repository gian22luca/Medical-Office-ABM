import Menu
from Validaciones import *


def consultas():
    """Número de Historia Clínica, Diagnóstico, Fecha (con formato AAAAMMDD)"""
    print("---------Consulta---------")
    try:
        archivo = open("datosPacientes.txt", "r")
        archivoConsultas = open("consultas.txt","a")
        numeroHC = input("Ingresar número de historia clínica: ")
        numeroHC = validar_int(numeroHC)
        
        while numeroHC == False and numeroHC != -1:
            print("NÚMERO DE HISTORIA CLINICA INVALIDO.")
            numeroHC = input("Ingresar número de historia clínica: (-1 para salir): ")
            numeroHC = validar_int(numeroHC)           
        existe = False
        while existe == False and numeroHC != -1:
            for linea in archivo:
                numeroHCE = linea.split(",")[0]
                if str(numeroHC) == numeroHCE:
                    print("Número ya registrado")
                    existe = True
                    break
            archivo.seek(0)
            if not existe:
                print("Número no existente.")
                numeroHC = int(input("Ingresar número de historia clínica: (-1 para salir): "))
                
        while numeroHC != "":
            diagnostico = input("Tipo de diagnostico?: ")
            diagnostico = validar_string(diagnostico)
            while diagnostico == False and diagnostico != -1:
                print("DIAGNOSTICO INVALIDO")
                diagnostico = input("Tipo de diagnostico? (-1 para salir): ")
                diagnostico = validar_string(diagnostico)
            if diagnostico == -1: #salgo de la funcion
                return  
            año = int(input("Ingresar el/los año/s:"))
            año = validar_año(año)
            mes = int(input("Ingresar el/los mes/es: "))
            mes = validar_mes(mes)
            dia = validar_dia(mes,año)
            archivoConsultas.write(f"{numeroHC}"+","+f"{diagnostico.upper()}"+","+f"{año:04d}{mes:02d}{dia:02d}"+"\n")
            print("Consulta cargada con exito  "+"\n")
            numeroHC = input("Ingresa numero Historia clinica (enter p/salir): ")

    except FileNotFoundError:
        print("ERROR")

    finally:
        try:
            archivo.close()
            archivoConsultas.close()
        except NameError:
            pass

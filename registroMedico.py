import Menu
from Validaciones import *

def datosPacientes():
    try:
        puO = input("Ingresar prepaga u obra social (enter para salir): ")
        puO = validar_string(puO)
        while puO == False and puO != -1:
                print("prepaga INVALIDA")
                puO = input("Ingresar prepaga (-1 para salir): ")
                puO = validar_string(puO)
        if puO == -1 :
            return
        
        while puO != "":
            nA = input("Ingresar nombre y apellido del paciente: ")
            nA = validar_string(nA)
            while nA == False and nA != -1:
                print("NOMBRE INVALIDO")
                nA = input("Ingresar nombre (-1 para salir): ")
                nA = validar_string(nA)
            if nA == -1: #salgo de la funcion
                return

            numHC = input("Ingresar número de historia clínica: ")
            numHC = validar_int(numHC)
            while numHC == False and numHC != -1:
                print("NÚMERO DE HISTORIA CLINICA INVALIDO.")
                numHC = input("Ingresar nombre (-1 para salir): ")
                numHC = validar_int(numHC)
            if numHC == -1: 
                return            
    
            existe = False
            archivo = open("datosPacientes.txt", "r")
            for linea in archivo:
                numHCE = linea.split(",")[0]
                if str(numHC) == numHCE:
                    print("Número existente")
                    existe = True
                    break
                      
            if not existe:
                archivo = open("datosPacientes.txt", "a")
                archivo.write(f"{numHC},{nA.upper()},{puO}\n")
                print("Paciente agregado con exito!")

            puO = input("Ingresar prepaga u obra social (enter para salir): ")

    except FileNotFoundError:
        print("ERROR!!!")
    finally:
        try:
            archivo.close()
        except NameError:
            pass










from registroMedico import *
from Login import CheckearLogin
from RegistroConsultas import *
from Busqueda import *
from Validaciones import *
from time import sleep

def LogIn():
    contador = 3
    print("Por favor ingrese su usuario y contraseña para acceder al sistema")
    while contador != 0 and contador != 4:
        usuario = input("Usuario:  ")
        contraseña = input("Contraseña:  ")
        if CheckearLogin(usuario, contraseña):
            mensaje_bienvenida()
            contador = 4
            MostrarMenu()
        else:
            contador -= 1
            print("El usuario no existe. Intentos restantes:", contador)
            print()
 
def mensaje_bienvenida(): 
    text = "\nBienvenido a la Clinica  \n"
    for c in text:
        print(c, end= ' ')
        sleep(0.1)
    
def mensaje_salida(): 
    text = "Cerrando programa\n"
    for c in text:
        print(c, end= ' ')
        sleep(0.1)
        

def abriendo(): 
    text = "\nAbriendo ..\n"
    for c in text:
        print(c, end = '')
        sleep(0.05)

def MostrarMenu():
    global seguirPrograma
    seguirPrograma = True
    while(seguirPrograma):
        try:
            print("Ingrese la operacion a realizar")
            print("     1-Carga de Paciente")
            print("     2-Carga de Consulta")
            print("     3-Busqueda")
            print("     0-Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                abriendo()
                datosPacientes()
            elif opcion == 2:
                abriendo()
                consultas()
            elif opcion == 3:
                abriendo()
                busqueda()
            elif opcion == 0:
                mensaje_salida()
                seguirPrograma = False
            else:
                pass
        except ValueError:
            pass


if __name__ == '__main__':
    LogIn()
if LogIn == True:
    mensaje_bienvenida()
    

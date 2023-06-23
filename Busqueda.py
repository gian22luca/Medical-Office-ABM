import Menu
from Validaciones import *

def crearMatriz(matriz, filas, columnas):
    for f in range(filas):
        matriz.append([0] * columnas)   
    return matriz

def rellenar_matriz(matriz, numeroFila, numeroHC, nombrePaciente, prepaga):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz[numeroFila][0] = numeroFila 
    matriz[numeroFila][1] = numeroHC
    matriz[numeroFila][2] = nombrePaciente
    matriz[numeroFila][3] = prepaga
    return matriz

def rellenar_matriz_consulta(matriz, numeroFila, numeroHC, diagnostico, fecha):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz[numeroFila][0] = numeroHC
    matriz[numeroFila][1] = diagnostico
    matriz[numeroFila][2] = fecha
    return matriz


def ordenarMatriz(m):
    matriz_ordenada = sorted(m, key=lambda x: x[2], reverse=True)
    
    return matriz_ordenada


def imprimir_matriz(matriz, f=0, c=0):
    if f == len(matriz):
        return
    print("%30s" % str(matriz[f][c]), end="")
    if c == len(matriz[0]) - 1:
        print()
        imprimir_matriz(matriz, f + 1, 0)
    else:
        imprimir_matriz(matriz, f, c + 1)


def busqueda():
    
    try:
        archivoPacientes = open("datosPacientes.txt", "r")
        archivoConsultas = open("consultas.txt", "r")
        nombre_buscado = input("Ingrese el nombre del paciente (todo o parte): ")
        pacientes_encontrados = []
        consultas_paciente = []

        for linea in archivoPacientes:
            datos = linea.split(",")
            numeroHC = datos[0]
            nombrePaciente = datos[1]
            prepaga = datos[2]
            
            if nombre_buscado.lower() in nombrePaciente.lower():
                pacientes_encontrados.append((numeroHC, nombrePaciente, prepaga))
                
        for linea in archivoConsultas:
            datos2 = linea.split(",")
            numeroHC2 = datos2[0]
            consultaDiagnostico = datos2[1]
            consultaFecha = datos2[2]
            consultas_paciente.append((numeroHC2,consultaDiagnostico,consultaFecha))
            
        print("Pacientes encontrados:")
        matriz_paciente = [["Identificador","Numero de Historia Clinica","Nombre y Apellido","Prepaga"]]
        matriz = crearMatriz(matriz_paciente, len(pacientes_encontrados), 4)
        
        contador = 1
        for numero, nombre, prep in pacientes_encontrados:
            rellenar_matriz(matriz, contador, numero, nombre, prep)
            contador = contador + 1
        imprimir_matriz(matriz)     
        seleccion = int(input("Seleccione un paciente (ingrese el número correspondiente): "))
        
        if seleccion > 0 and seleccion <= len(pacientes_encontrados):
            numeroHC, nombrePaciente, prepaga = pacientes_encontrados[seleccion - 1]
            print(f"\nConsultas del paciente:\n Número de Historia Clínica: {numeroHC}\n Nombre: {nombrePaciente}\n Prepaga: {prepaga}\n")
            print("Listado de consultas:")
                     
        contadorDiagnosticos = 0
        for i in consultas_paciente :
            num = i[0]
            if num == numeroHC :
                contadorDiagnosticos = contadorDiagnosticos + 1
        archivoPacientes.seek(0)
        matriz_consulta = [["Numero de Historia Clinica", "Diagnostico", "Fecha"]]
        matriz2 = crearMatriz(matriz_consulta, contadorDiagnosticos, 3)
        
        contador = 1
        for num, diagnostico, fecha in consultas_paciente:
             if num == numeroHC:
                rellenar_matriz_consulta(matriz_consulta, contador, num, diagnostico, fecha)
                contador = contador + 1
        matriz_ordenada = ordenarMatriz(matriz_consulta)
        imprimir_matriz(matriz_ordenada)
        
    except FileNotFoundError:
        print("ERROR")
        
    finally:
        try:
            archivoPacientes.close()
            archivoConsultas.close()
        except NameError:
            pass
        
      




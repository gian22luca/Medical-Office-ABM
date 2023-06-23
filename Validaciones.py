import calendar



def validar_int(x):
        if x == '-1':
            return int(x)
        if x.isdigit():
            return int(x)
        else:
            return False

def validar_string(x):
    if x == "-1":
        return int(x)
    elif x.replace(' ', '').isalpha():
        return x
    else:
        return False
    
def validar_dia(mes,año):
    max_dias = calendar.monthrange(año, mes)[1]
    print("\n",calendar.month(año,mes))
    dia = input("\ningresar dia (-1 para salir): ")
    dia = validar_int(dia)
    while dia < 1 and dia != -1 or dia > max_dias or dia == False:
        print("\nDIA INVALIDO")
        print("\n",calendar.month(año,mes))
        dia = input("ingresar dia (-1 para salir): ")
        dia = validar_int(dia)
    return dia

def validar_mes(mes):
    #valida si el mes es menor que 1 pero no -1 o el mes es mayor que 12
    while mes < 1 and mes != -1 or mes > 12 or mes == False:
        print("MES INVALIDO")
        mes = input("ingresar mes (-1 para salir): ")
        mes = validar_int(mes)
    return mes


def validar_año(año):
    while año < 2000 and año != -1 or año > 2023 or año == False:
        print("AÑO INVALIDO")
        año = input("ingresar año (-1 para salir): ")
        año = validar_int(año)
    return año
        
     
     
     
     
     
def Opciones():
    print("1-) Suma \n2-) Resta \n3-) Multiplicacion \n4-) Divicion")

    opcion = int(input("Operacion a realizar: "))
    return opcion

def Suma (x, y):
    try:
        print("Suma:\n", x + y)
    except:
        print("Hay un error que esta evitando que el programa se ejecute")
    finally:
        print("Programa finalizado")

def Resta(x, y):
    try:
        print("Resta: \n", x - y)
    except:
        print("Hay un error que esta evitando que el programa se ejecute")
    finally:
        print("Programa finalizado")

def Multiplicacion(x, y):
    try:
        print("Multiplicacion: \n", x * y)
    except:
        print("Hay un error que esta evitando que el programa se ejecute")
    finally:
        print("Programa finalizado")

def Divicion(x, y):
    try:
        print("Divicion: \n", x / y)
    except:
        print("Hay un error que esta evitando que el programa se ejecute")
    finally:
        print("Programa finalizado")


i = 0
while i == 0:
    opc = Opciones()
    if opc == 1:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        Suma(valor1, valor2)
    elif opc == 2:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        Resta(valor1, valor2)
    elif opc == 3:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        Multiplicacion(valor1, valor2)
    elif opc == 4:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        Divicion(valor1, valor2)
    elif opc == 5:
        i = 1
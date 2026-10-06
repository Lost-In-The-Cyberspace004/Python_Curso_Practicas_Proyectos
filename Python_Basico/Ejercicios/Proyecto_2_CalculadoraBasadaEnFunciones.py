def calculos(x, y):
    return suma(x, y), resta(x, y), multiplicacion(x, y), divicion(x, y)

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def divicion(x, y):
    return x / y

i = 0
while i == 0:

    valor1 = float(input("Valor 1: "))
    valor2 = float(input("Valor 2: "))

    if valor1 == 0 and valor2 == 0:
        i = 1
    else:
        s, r, m, d = suma(valor1, valor2), resta(valor1, valor2), multiplicacion(valor1, valor2), divicion(valor1, valor2)
        print(s)
        print(r)
        print(m)
        print(d)
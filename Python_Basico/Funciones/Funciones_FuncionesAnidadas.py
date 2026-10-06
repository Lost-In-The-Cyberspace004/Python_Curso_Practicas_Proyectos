def sumarRestar(x, y):
    return sumar(x, y), restar(x, y) #funciones anidadas
def sumar(x, y):
    return x + y
def restar(x, y):
    return x - y

valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
suma, resta = sumarRestar(valor1, valor2)
print(suma)
print(resta)
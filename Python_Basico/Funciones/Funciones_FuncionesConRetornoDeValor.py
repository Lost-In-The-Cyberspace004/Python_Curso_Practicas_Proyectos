#Para retornar un valor usamos return y asignamos el metodo a una variable

def sumar(x, y):
    return x + y

valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
operacion = sumar(valor1, valor2) #Como se dijo: se asigna el valor de retorno a una variable
print(operacion)
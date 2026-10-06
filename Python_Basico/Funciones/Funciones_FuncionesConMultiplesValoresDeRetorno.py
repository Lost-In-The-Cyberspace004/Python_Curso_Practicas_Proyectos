def FuncionConDobleValorDeRetorno(x, y):
    return x + y, x - y
numero1 = float(input("Valor 1: "))
numero2 = float(input("Valor 2: "))
OperacionesSuma, OperacionesResta = FuncionConDobleValorDeRetorno(numero1, numero2)
print(OperacionesSuma)
print(OperacionesResta)
def FuncionesConMultiplesParametros(*Valores):
    resultado = 0
    for i in Valores:
        resultado = resultado + i
    return resultado

Operacion = FuncionesConMultiplesParametros(2, 2, 2, 45, 2334)
print(Operacion)
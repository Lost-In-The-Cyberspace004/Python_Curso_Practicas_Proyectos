#Los parametros son los valores que van dentro de los ()

def MayorQue(param):
    if(param > 0): 
        if(param > 10):
            print("Mayor que 10")
        else:
            print("No es mayor que 10")
    else:
        print("No es mayor que 0")

valorDeParametro = int(input("Ingrese un valor: "))
MayorQue(valorDeParametro)
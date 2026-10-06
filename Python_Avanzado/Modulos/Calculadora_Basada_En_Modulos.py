import Operaciones #IMPORTAMOS EL OTRO ARCHIVO CREADO

i = 0 

while i == 0:
    opcion = int(input("1-) suma \n2-) Resta \n3-) Multiplicacion \n4-) Divicion \nOpcion: "))

    a = 5
    b = 7

    print("======\n",a)
    print(b,"\n======")

    if opcion == 1:
        print(Operaciones.suma(a, b))
    elif opcion == 2:
        print(Operaciones.resta(a, b))
    elif opcion == 3:
        print(Operaciones.multiplicacion(a, b))
    elif opcion == 4:
        print(Operaciones.divicion(a, b))

    else:
        print("Opcion inexistente")
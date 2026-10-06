i = 0
numero1 = 0
numero2 = 0
while i == 0:
    print("Suma")
    print("Resta")
    print("Multiplicacion")
    print("Divicion")

    opcion = int(input("Opcion: "))
    if opcion > 0:
            if opcion == 1:
                numero1 = float(input("primer numero: "))
                numero2 = float(input("segundo numero: "))
                suma = numero1 + numero2
                print("R: ", suma)
            elif opcion == 2:
                numero1 = float(input("primer numero: "))
                numero2 = float(input("segundo numero: "))
                resta = numero1 - numero2
                print(resta)
            elif opcion == 3:
                numero1 = float(input("primer numero: "))
                numero2 = float(input("segundo numero: "))
                Multiplicacion = numero1 * numero2
                print(Multiplicacion)
            elif opcion == 4:
                numero1 = float(input("primer numero: "))
                numero2 = float(input("segundo numero: "))
                divicion = numero1 / numero2
                print(divicion)
            elif opcion == 5:
                i = 1
    else:
         print("No puedes operar valores negativos")
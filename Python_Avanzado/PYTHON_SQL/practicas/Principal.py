from Control import ControlDeSistemas

Obj1 = ControlDeSistemas()

i = 0

while i == 0:
    print("--------------------")
    Opcion = int(input("1-) Ver contenido \n2-) Insertar contenido \n3-) Eliminar contenido \n4-) Buscar valores \n5-) Editar valores \n-------------------- \nOpcion: "))

    if Opcion == 1:

        print(Obj1.VerContenido())

    elif Opcion == 2:

        Producto = input("Producto: ")
        Precio = float(input("Precio: "))
        Cantidad = float(input("Cantidad: "))

        Obj1.InsertarContenido("\n",Producto, Precio, Cantidad)

    elif Opcion == 3:
        
        ID = int(input("ID: "))
        Obj1.EliminarContenido(ID)

    elif Opcion == 4:

        print(Obj1.BuscarValores())

    elif Opcion == 5:

        ID = int(input("ID: "))
        Producto = input("Producto: ")
        Precio = float(input("Precio: "))
        Cantidad = float(input("Cantidad: "))

        Obj1.EditarValores(ID, Producto, Precio, Cantidad)
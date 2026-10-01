import tkinter 

ventana = tkinter.Tk() #Creamos la ventana
ventana.geometry("300x300+950+50") #Las dimenciones de la ventana y donde se va a generar
ventana.title("Titulo de una ventana") #TITULO DE LA VENTANA
ventana.iconbitmap("Logo.ico") #PONER UN LOGO
ventana.resizable(False, False) #ELIMINAMOS EL RESIZABLE

#ETIQUETAS
etiqueta = tkinter.Label(ventana, text = "Hola mundo") #ETIQUETA DE TEXTO
etiqueta.pack() #USAMOS PACK PARA INSERTAR EL ELEMENTO EN LA VENTANA
etiqueta.pack(side=tkinter.BOTTOM) #UBICAMOS LOS ELEMENTOS EN DIFERENTES COORDENADAS
etiqueta.grid(row=2, column=0) #USAMOS COLUMNAS Y FILAS PARA POSICIONAR DINAMICAMENTE
#TOP, LEFT, RIGHT, BUTTON
etiqueta = tkinter.Label(ventana, bg = "blue") #PODEMOS PONERLE COLORES



#PODEMOS ESTIRAR LOS ESPACIOS, ES DECIR EL ESPACIO QUE OCUPA EL ELEMENTO
etiqueta.pack(fill = tkinter.X)
etiqueta.pack(fill = tkinter.Y, expand = True) #PARA EL EJE Y
etiqueta.pack(fill = tkinter.BOTH, expand = True) #PARA QUE OCUPE TODO EL ESPACIO EN LA VENTANA



#CREAMOS UN BOTON
boton1 = tkinter.Button(ventana, text = "click")
boton1 .pack()
boton2 = tkinter.Button(ventana, padx=40, pady= 40) #TAMANIO DEL BOTON



#EVENTOS DE LOS BOTONES
def saludar():
    print("hola")
boton3 = tkinter.Button(ventana, text = "presioname", command=saludar) #OBSERVA COMO SE LLAMA AL METODO SIN PARENTESIS Y CON COMAND



#PASO DE VALORES POR PARAMETROS
def saludar(nombre):
    print("hola " + nombre)
boton4 = tkinter.Button(ventana, text = "presioname", command = lambda: saludar()) #CUANDO VAYEMOS A PASAR VALORES POR PARAMETROS USAMOS LAMBDA



#CREACION DE ENTRADAS DE USUARIO
CajadeTexto1 = tkinter.Entry(ventana)
CajadeTexto1.pack()
CajadeTexto2 = tkinter.Entry(ventana, font= "helvetica 50") #ALTERAMOS SU FUENTE Y TAMANIO DE TEXTO



#OBTENER TEXTO DE UNA ENTRADA DE USUARIO
def textoPrueba():
    ValorEntrUs = CajadeTexto1.get() #OBTENEMOS EL VALOR DE LA ENTRADA DE USUARIO
    #PARA MOSTRARLO EN UNA ETIQUETA DE TEXTO EN VENTANA (LABEL)
    etiqueta["text"] = ValorEntrUs



#Para insertar usamos tk.StringVar() aunque tambien existe IntVar() o FloatVar()
texto = tkinter.StringVar()
CajaDeTextoInsertar = tkinter.Entry(ventana, textvariable = texto)
texto.set("Hola")



#PARA PONER UNA IMAGEN
imagen = tkinter.PhotoImage(file = "Carpeta/Imagen.png")
#INSERTARLA
label = tkinter.Label(image=imagen)
label.pack()



#MENU DESPLEGABLE
# Opción seleccionada por defecto
opcion_seleccionada = tkinter.StringVar(ventana)
opcion_seleccionada.set("Opción 1") # Valor inicial
# Crear el menú desplegable
opciones = ["Opción 1", "Opción 2", "Opción 3"]
desplegable = tkinter.OptionMenu(ventana, opcion_seleccionada, *opciones)
desplegable.pack()



#BOTONES DE SELECCION
opcion_radio = tkinter.StringVar(value="1") # Controla el grupo
# Varios radio buttons vinculados a la misma variable
radio1 = tkinter.Radiobutton(ventana, text="Modo Normal", variable=opcion_radio, value="1")
radio2 = tkinter.Radiobutton(ventana, text="Modo Experto", variable=opcion_radio, value="2")
radio1.pack()
radio2.pack()



ventana.mainloop() #El main loop controla el bucle de la ventana
#Como en un videojuego
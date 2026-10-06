class autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def mostrarAutor(self):
        print(self.Nombre, " / ", self.Apellidos)






class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn

    def AgregarAutor (self, autor):
        self.Autor = autor

    def MostrarTodo(self):
        print("Titulo: ", self.Titulo)
        print("ISBN: ", self.ISBN)
        print("Autor: ", self.Autor.mostrarAutor())

    def ObtenerTitulo(self):
        return self.Titulo






class biblioteca:
    def __init__(self):
        self.listaLibros = []

    def numeroLibros(self):
        return len(self.listaLibros)

    def AgregarLibros(self, libro):
        self.listaLibros = self.listaLibros + [libro]

    def MostrarBiblioteca(self):
        for i in self.listaLibros:
            i.MostrarTodo()

    def borrarLibro(self, titulo):
        econtrado = False 
        posicionABorrar = -1 #Esta variable nos devolvera la posicion donde se almacena el contenido
        for i in self.ListaLibros: #i es el objeto o contenedor de la informacion, no el indice o iterador
            posicionABorrar += 1
            if i.ObtenerTitulo() == titulo:
                encontrado = True
                break
        if encontrado:
            del self.ListaLibros[posicionABorrar] #Cuando la encontramos, eliminamos esa posicion, que se traduce tambien a borrar su contenido
            print(titulo, "borrado")






def MostrarMenu():
    print(" 1-) agregar libro \n 2-) Mostrar biblioteca \n 3-) Borrar libro \n 4-) Numero de libros \n 5-) Salir")





#En las siguientes funciones, asignamos el objeto creado mas abajo como parametro para acceder a la clase biblioteca, ya que muchas de las funciones funcionan en esa clase
def IngresarValores(Mi_Biblioteca):
    NombreDelAutor = input("Nombre del autor: ")
    ApellidoDelAutor = input("Apellido del autor: ")
    NombreDeLibro = input("Nombre del libro: ")
    ISBN = input("Isbn: ")

    nuevoAutor = autor(NombreDelAutor, ApellidoDelAutor)
    AgregarLibro = Libro(NombreDeLibro, ISBN)

    Mi_Biblioteca.AgregarLibros(AgregarLibro) #Llamamos al objeto que en este caso es un parametro y asignamos el objeto
    AgregarLibro.AgregarAutor(nuevoAutor)





def MostrarBiblioteca(Mi_Biblioteca):
    Mi_Biblioteca.MostrarBiblioteca()






def EliminarLibros(Mi_Biblioteca):
    ElementoAborrar = input("Libro a borrar: ")
    Mi_Biblioteca.borrarLibro(ElementoAborrar)






def NumeroDeLibros(Mi_Biblioteca):
    return Mi_Biblioteca.numeroLibros()






mi_Biblioteca = biblioteca() #Tenemos que crear el objeto para conectarnos a la clase biblioteca y asi poder acceder a sus metodos
i = 0






while i == 0:    
    MostrarMenu()
    Opcion = int(input("Opcion: "))
    if Opcion == 1:
        IngresarValores(mi_Biblioteca) #Pasamos por parametros el objeto creado arriba
    elif Opcion == 2:
        MostrarBiblioteca(mi_Biblioteca)
    elif Opcion == 3:
        EliminarLibros(mi_Biblioteca)
    elif Opcion == 4:
        print(NumeroDeLibros(mi_Biblioteca))
    elif Opcion == 5:
        i = 1
        break
print("Terminado...")
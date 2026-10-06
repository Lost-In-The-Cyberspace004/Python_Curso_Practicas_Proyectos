#Funciones
def my_function():
    print("Esto es una funcion")

#llamamos a la funcion
my_function()

for i in range(10):
    my_function()

#funciones con retorno
def my_function2():
    return 10
print(my_function2())

#funciones con parametros
def my_function3(x , y):
    return x + y
print(my_function3(3, 3))

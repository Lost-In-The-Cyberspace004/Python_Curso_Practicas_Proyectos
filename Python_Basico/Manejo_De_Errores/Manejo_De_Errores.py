try: #codigo que se ejecuta si todo sale bien
    print(3 / 0)
except: #Error presentado
    print("Error")
else: #else usado para avisar de otras cosas
    print("No se han producido errores")
finally: #finalizacion del programa
    print("Programa acabado")
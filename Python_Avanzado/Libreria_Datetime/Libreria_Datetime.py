import datetime
print("Ahora mismo es: ", datetime.datetime.now())
print("Hoy es: ", datetime.date.today())
fecha = datetime.date(2017,11,29)
print(fecha)
fechahora = datetime.datetime(2016,2,21,14,00,00,000)
print(fechahora)

#Para poder acceder a cada elemento
fecha = datetime.datetime(2016,2,21,14,00,00,000)
print(fecha)
print("Año: ",fecha.year)
print("Mes: ",fecha.month)
print("Día: ",fecha.day)
print("Hora: ",fecha.hour)
print("Minutos: ",fecha.minute)
print("Segundos: ",fecha.second)
print("Microsegundos: ",fecha.microsecond)
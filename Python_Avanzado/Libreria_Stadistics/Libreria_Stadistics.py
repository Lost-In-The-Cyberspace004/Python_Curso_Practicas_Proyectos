import statistics
import random
valores = random.sample(range(10), 8)
print("Número aleatorios generados: ", valores)


print("Media: ", statistics.mean(valores))
print("Mediana: ", statistics.median(valores))
print("Mediana inferior: ", statistics.median_low(valores))
print("Mediana superior: ", statistics.median_high(valores))
print("Moda: ", statistics.mode(valores))
print("Varianza: ", statistics.variance(valores))
from Densidad import density_per_km2
from Poblacion import total_population
from densidad_M2 import density_per_m2
import pandas as pd
import matplotlib.pyplot as plt

cities = pd.read_csv("lista.csv")
print(cities)
print("------------")
print(density_per_km2(cities))
print("------------")
print(total_population(cities))
print("---------------")
print(density_per_m2(cities))

# llama las funciones
city_pop = total_population(cities)
density_km2 = density_per_km2(cities)
density_m2 = density_per_m2(cities)
# Plot resultados
plt.figure()
city_pop.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.legend(title='City')
plt.title('Population by City')
plt.show()

plt.figure()
density_km2.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.legend(title='City')
plt.title('Density KM2 by City')
plt.show()

plt.figure()
density_m2.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.legend(title='City')
plt.title('Density  M2 by City')
plt.show()



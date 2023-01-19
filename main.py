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
plt.figure(num="Grafica 1")
city_pop = ["Manila ", "Mandaluyong", "pateros", "Caloocan ", "ben fren ", "Katmandu ", "Dakka", "Makati", "Manhattan", "Port-au-Prince"]
Population = [1661584, 8906136, 1442000, 629616, 425758, 1628701, 1846513, 98731, 212646, 65227]
plt.pie(Population, labels=city_pop, autopct="%0.1f %%")
plt.axis("equal")
plt.show()

plt.figure(num="Grafica 2")
city_pop = ["Manila ", "Mandaluyong", "pateros", "Caloocan ", "ben fren ", "Katmandu ", "Dakka", "Makati", "Manhattan", "Port-au-Prince"]
density_km2 = [43062, 38495, 37061, 31233, 30001, 29161, 29069, 28975, 27544, 27395]
plt.pie(density_km2, labels=city_pop, autopct="%0.1f %%")
plt.axis("equal")
plt.show()

plt.figure(num="Grafica 2")
city_pop = ["Manila ", "Mandaluyong", "pateros", "Caloocan ", "ben fren ", "Katmandu ", "Dakka", "Makati", "Manhattan", "Port-au-Prince"]
density_m2 = [111532, 99703, 95988, 80893, 77702, 75526, 75289, 75044, 7134, 70953]
plt.pie(density_m2, labels=city_pop, autopct="%0.1f %%")
plt.axis("equal")
plt.show()

fig1 = plt.figure(num="Grafica 1")
fig2 = plt.figure(num="Grafica 2")
fig3 = plt.figure(num="Grafica 3")
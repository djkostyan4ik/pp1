import matplotlib.pyplot as plt
temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(temperatures.keys())
temperatures_values = list(temperatures.values())

plt.bar(cities,temperatures_values)

plt.title('Temperatures Recorded in cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

plt.show()
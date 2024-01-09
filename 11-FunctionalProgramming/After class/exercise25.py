temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
temperatures = list(filter(lambda x: x[1]>0, temp.items()))
print(f'Cities with positive temperatures: {[x[0] for x in temperatures]}')
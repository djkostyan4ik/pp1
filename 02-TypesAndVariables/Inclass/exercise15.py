temp_in_cel = int (input ('Write the current temperature in your city: '))
temp_in_kel = temp_in_cel + 273.15 #calculates the the temperature in kelvin with the help of cilcius temperature
temp_in_fahren = (temp_in_cel * 9) / 5 + 32 # calculates the temperature in fahrengeits with the help of cilcius temperature
print (temp_in_fahren)
print (temp_in_kel)
import math


first_side = int(input ( 'Enter the length of the first side ' ))
second_side = int(input ( 'Enter the length of the second side ' ))
third_side = int(input ( 'Enter the length of the third side ' ))

s = (first_side + second_side + third_side) / 2
S = first_side + second_side + third_side

area = math.sqrt(s * (s - first_side)*(s - second_side)*(s - third_side))
print(area)
print (S)
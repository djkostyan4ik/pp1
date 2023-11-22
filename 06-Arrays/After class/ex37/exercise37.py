import MyArrays
array = [7,3,8,5,2]
print("Numbers:",','.join(map(str,array)))
sec_larg = MyArrays.second_largest_element([7, 3, 8, 5, 2])
print("Second largest number:",sec_larg)

difference = MyArrays.my_difference([7, 3, 8, 5, 2])
print("Difference:",difference)

median_value = MyArrays.my_median([7, 3, 8, 5, 2])
print("Median:",median_value)

two_el_arr = MyArrays.my_array([7, 3, 8, 5, 2])
print("Smallest and largest number:",','.join(map(str,two_el_arr)))

separated_arr = MyArrays.separated([7, 3, 8, 5, 2])
print("Numbers as a string:",'-'.join(map(str,separated_arr)))
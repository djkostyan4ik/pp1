import random
array = [1, 3, 5, 6, 7, 9, 24]
def rand_elem(array):
    random_index = random.randint(0,len(array)-1)
    return array[random_index]

print(rand_elem(array))
print(rand_elem(array))
print(rand_elem(array))
print(rand_elem(array))
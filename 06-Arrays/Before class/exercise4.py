import sys
import timeit

list_eg = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]
tuple_eg = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

list_test = timeit.timeit(stmt = "[1, 2, 3, 4, 5]", number = 1000000)
tuple_test = timeit.timeit(stmt = "(1, 2, 3, 4, 5)", number = 1000000)

print('List time: ', list_test)
print('Tuple time: ', tuple_test)
import random
# a
arr1 = [3, 7, 1, 0, 4]
print(arr1)
# b
arr2 = [
    [2, 3],
    [7, 1],
    [0, 4]
]
print(arr2)
# c
arr3 = [7 for i in range(5)]
print(arr3)
# d
arr4 = [i for i in range(1,10)]
print(arr4)
# e
arr5 = [i * 2 for i in range (1,10)]
print(arr5)
# f
arr6 = [random.randint(1,20) for i in range(10)]
print(arr6)
# g
arr7 = [[] for i in range(5)]
print(arr7)
# h
arr8 = [[1 for i in range(2)] for j in range(4)]
print(arr8)
# i
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(arr9)
# j
arr10 = [4, 0, 3]
print(arr10)
# k
arr11 = [0 for i in range(15)]
print(arr11)
# l
arr12 = [i for i in range(1,30)]
print(arr12)
# m
arr13 = [random.randint(0,1) for i in range(20)]
print(arr13)
# n
rows, columns = (5, 2)
# arr14 = [[False] * columns] * rows
arr14 = [[False for i in range(2)] for j in range(5)]
print(arr14)

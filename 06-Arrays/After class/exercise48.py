def create_2d_arr(x,y):
    arr = []
    for i in range(y):
        a = []
        for j in range (x):
            a.append(0)
        arr.append(a)
    return arr
print(create_2d_arr(3,5))
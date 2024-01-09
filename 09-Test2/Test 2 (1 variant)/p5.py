def f(arr2D):
    count = 0
    for row in arr2D:
        if row[0] ** 2 == row[1]:
            count += 1
    return count

if __name__ == '__main__':
    print(f([[4,16], [3,9], [-3,9]]))
    print(f([[4,15], [3,9], [-3,-9]]))
def f(arr2D):
    count = 0
    for row in arr2D:
        if row[0] > 0 and row[1] > 0:
            count += 1
        else:
            continue
    return count
if __name__ == '__main__':
    print(f([[1,4],[8,5]]))
    print(f([[7,5],[4,-5],[1,9],[4,4]]))
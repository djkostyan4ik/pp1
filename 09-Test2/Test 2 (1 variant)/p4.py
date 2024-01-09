def f(arr):
    result = 0
    for elem in arr:
        if arr.count(elem) == 1:
            result += 1
        else:
            continue
    return result

if __name__ == '__main__':
    print(f([11,22,33,11]))
    print(f([11,22,11,11,22,35,27,11,22,14]))

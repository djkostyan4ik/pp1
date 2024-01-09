def f(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
if __name__ == '__main__':
    print(f([25,25,23]))
    print(f([7,7,7,7,7,5,7,7]))
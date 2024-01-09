def f(arr):
    if len(arr) < 3:
        exit()

    arr = sorted(arr)
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[len(arr)-1]

if __name__ == '__main__':
    print(f([7,7,7,7,7,5,7,7]))
    print(f([17,17,19,17,17,17,17]))
    print(f([3,3,3,3,3,3,4]))
    print(f([3,4]))
def f(arr):
    for number in arr:
        if arr.count(number) % 2 == 1:
            return number

def main():
    print(f([3,3,4,4,4,2,2,2,2]))
    print(f([6,6,6,6,4,4,5,2,2,2,2,2,2]))

if __name__ == '__main__':
    main()
def f(n):
    arr = []
    for digit in str(n):
        if int(digit) % 2 == 1:
            arr.append(int(digit))
    if len(arr) == 0:
        return -1
    maximum = max(arr)
    minimum = min(arr)
    result = maximum - minimum
    return result

def main():
    print(f(10852))
    print(f(7235973))
    print(f(4388))
    print(f(846206))

if __name__ == '__main__':
    main()
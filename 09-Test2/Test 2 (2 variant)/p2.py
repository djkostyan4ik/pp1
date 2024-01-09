def f(n):
    for i in n:
        count = n.count(i)
        if count % 2 != 0:
            return i
        else:
            continue

if __name__ == '__main__':
    print(f([7,7,7,7,4,4,4,5,5]))
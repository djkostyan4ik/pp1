def f(n):
    odds = []
    for j in str(n):
        if int(j) % 2 == 1:
            odds.append(int(j))
    if len(odds) == 0:
        return -1
    maximum = max(odds)
    minimum = min(odds)
    result = maximum - minimum
    return result
def main():
    print(f(10852))
    print(f(7235973))
    print(f(4388))
    print(f(846206))

if __name__ == '__main__':
    main()
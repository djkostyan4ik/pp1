def f(n):
    i = 5
    result = []
    if n <= 0:
        return ''
    else:
        result += str(n * '/')
    while i < len(result):
        result.insert(i,'-')
        i += 6
    return ''.join(result)        


    
def main():
    print(f(-4))
    print(f(0))
    print(f(5))
    print(f(7))
    print(f(10))
    print(f(11))

if __name__ == '__main__':
    main()
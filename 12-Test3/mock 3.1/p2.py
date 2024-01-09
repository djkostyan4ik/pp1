def f(x,y,digit):
    count = 0
    for number in range(x,y+1):
        count += str(number).count(str(digit))
    return count
def main():
    print(f(10,15,1))
    print(f(28,32,2))
    print(f(100,105,6))
    print(f(100,101,0))

if __name__ == '__main__':
    main()

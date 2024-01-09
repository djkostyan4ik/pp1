def f(x,y,d):
    for number in range(x,y+1):
        if d in str(number):
            return True
    return False
def main():
    print(f(10,15,"14"))
    print(f(100,120,"11"))
    print(f(205,210,"04"))
            
if __name__ == '__main__':
    main()


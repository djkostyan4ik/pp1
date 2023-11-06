def f(x,y):
    result = 0
    for i in range(x,y):
       if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
           result += i
    return result
    
if __name__ == '__main__':
    print(f(1,20))
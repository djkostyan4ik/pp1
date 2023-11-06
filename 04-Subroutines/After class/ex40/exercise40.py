def f(number):
    result = 0
    for i in range (1, 10):
        count = 0
        for a in str(number):
            if int(a) == i:
                count += 1
        if count > 1:
            result += i * count        
    return result


if __name__=="__main__":
#    print(f(1027))
    print(f(230335))
    print(f(513553007))
    

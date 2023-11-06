def f(dice):
    result = ''
    max = 0
    for i in dice:
        count = 0 
        for a in dice:
            if i == a:
                count += 1
        if count > max:
            result = i
            max = count
    return result

if __name__ == '__main__':
    print(f('2133'))
    print(f("5233165554211"))
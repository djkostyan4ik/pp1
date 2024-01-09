import re
def f(t):
    my_sum = 0
    result = re.findall(r'-?\d+', t)
    for elem in result:
        if int(elem) < 0:
            continue
        else:
            my_sum += int(elem)

    return my_sum

if __name__ == '__main__':
    print(f('11 and 4 is 15'))
    print(f('water12, and 3play is not 8'))
    print(f('water-12 book15 -3'))

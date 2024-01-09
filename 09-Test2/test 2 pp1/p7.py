def f(d,c):
    count = 0
    words = d.keys()
    for word in words:
        if word[0] == c[0] and word[1] == c[1]:
            count += 1
    return count

if __name__ == '__main__':
    print(f({'xyz': 123},'zyx'))
    print(f({'bccga': True, 'def': 7,'bcd': 'xyz'},'bc'))
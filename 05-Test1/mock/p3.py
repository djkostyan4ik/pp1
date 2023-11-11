def f (name):
    a = ''
    result = name[0]
    for i in name:
        if a == ' ':
            result += i
        a = i
    return result

if __name__ == '__main__':
    print(f('Internet of Things'))
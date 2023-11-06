def f(sentence):
    result = ''
    for i in sentence:
        if i != ' ':
            result += i

    return result

if __name__ == '__main__':
    print(f('integrated development environment'))
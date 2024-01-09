def f(word):
    if len(word) == 0:
        return ''
    else:
        word = word.lower()
    arr = []
    for index, letter in enumerate(word):
        if letter == ' ':
            continue
        else:
            arr.append(word[:index] + word[index].upper() + word[index + 1:])
    return '-'.join(arr)

def main():
    print(f('book'))
    print(f('water'))
    print(f('ok'))
    print(f('a'))
    print(f(''))
    print(f('     '))

if __name__ == '__main__':
    main()
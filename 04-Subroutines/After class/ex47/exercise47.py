def f(text):
    result = ''

    for i in text[0:1]:
        result += i
        for a in text[1:]:
            result += '-' + a

    return result


if __name__ == '__main__':
    print(f'("University") returns "{f('University')}"')
    print(f'("UE") returns "{f('UE')}"')
    print(f'("x") returns "{f('x')}"')
    print(f'("") returns "{f('')}"')
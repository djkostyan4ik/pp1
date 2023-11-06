def f(palindrome):
    reversed_expression = palindrome[::-1]
    if palindrome == reversed_expression:
        return True
    else:
        return False

if __name__ == '__main__':
    print(f('radar'))
    print(f('book'))
    print(f('12-11-21'))
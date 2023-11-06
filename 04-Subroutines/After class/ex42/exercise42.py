def f(number1, number2, number3):
    max_number = max(number1, number2, number3)
    min_number = min(number1, number2, number3)
    result = max_number - min_number
    return result


if __name__ == '__main__':
    print(f(7,4,9))
    print(f(2,12,8))
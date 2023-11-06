def f(n):
    result = ''
    for i in range(n):
        if i >= 1:
            result += '/'
        result += '*'
    return result
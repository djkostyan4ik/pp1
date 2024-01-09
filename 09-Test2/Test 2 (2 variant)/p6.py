
def f(t):
    hours, minutes = map(str, t.split(':'))
    if int(hours) < 12:
        period = 'am'
    else:
        period = 'pm'

    if int(hours) == 0:
        hours_12_format = 0
    elif int(hours) <= 12:
        hours_12_format = int(hours)
    else:
        hours_12_format = int(hours) - 12
    # if len(str(minutes)) < 2:
    #     minutes == f'0{minutes}'
    return f'{hours_12_format}:{minutes}{period}'
if __name__ == '__main__':
    print(f('23:05'))
    print(f('01:04'))
    print(f('00:23'))
# def f(n):
#     if int(n[0:2]) > 12:
#         n = str(int(n[0:2]) - 12) + ':' + n[3:5] + 'pm'
#     elif int(n[0:2]) == 0:
#         n = str(int(n[0:2]) + 12) + ':' + n[3:5] + 'pm'
#     else:
#         n = str(int(n[0:2])) + ':' + n[3:5] + 'am'
#     return n

# if __name__ == '__main__':
#     print(f('01:06'))
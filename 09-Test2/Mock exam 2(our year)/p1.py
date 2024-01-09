def f(player1, player2):
    result = 0
    result2 = 0
    val = ['A','K','Q','J','T']
    for i in player1:
        if i in val:
            result += 10
        else:
            result += int(i)
    for j in player2:
        if j in val:
            result2 += 10
        else:
            result2 += int(j)

    if result >= result2:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(f('AJ972','AQT72'))
    print(f('9532','K8'))
def f(c):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6','5','4','3','2']
    for sign in c:
        if sign in cards:
            cards.remove(sign)
    for i in cards:
        return i
if __name__ == '__main__':
    print(f('2345678JTQKA'))
    print(f('2K345AQJ967T'))
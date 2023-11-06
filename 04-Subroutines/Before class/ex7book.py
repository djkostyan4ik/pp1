
def computergarde(s):
    if s > 1.0:
        return 'Error: Out of range'
    elif s == 1.0:
        return 'A'
    elif s >= 0.9:
        return 'A'
    elif s >= 0.8:
        return 'B'
    elif s >= 0.7:
        return 'C'
    elif s >= 0.6:
        return 'D'
    elif 0.0 <= s < 0.6:
        return 'F'
    else:
        return 'Error'
score = input('Enter a score between 0.0 and 1.0: ')
try:
    s = float(score)
except:
    print('Bad score')
    quit()

print(computergarde(s))


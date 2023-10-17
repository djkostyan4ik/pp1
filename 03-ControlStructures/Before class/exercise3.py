score = input('Enter a score between 0.0 and 1.0: ')
try:
    s = float(score)
except:
    print('Bad score')
    quit()
if s > 1.0:
    print('Error: Out of range')
elif s == 1.0:
    print('A')
elif s >= 0.9:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
elif 0.0 <= s < 0.6:
    print('F')
else:
    print('Error')
def chop(t):
    del t[0]
    del t[-1]

def middle(t2):
    new = t2[1:]
    del new[-1]
    return new


t = [1, 2, 3, 4]
t2 = [1, 2, 3, 4]
print(chop(t))
print (middle(t2))
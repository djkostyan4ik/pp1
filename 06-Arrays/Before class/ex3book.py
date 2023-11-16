user_data = input('Which files? ')
fhand = open(user_data, 'r')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if (len(words) == 0 or len(words) < 3) or words[0] != 'From': continue
    print(words[2]) 
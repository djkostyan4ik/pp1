fname = input('File name: ')
fhand = open(fname)
options = ['','q','Q']
run = True
while run:
    for i in range(5):
        print(fhand.readline())

    x = input('Press Enter to continue, press Q to quit: ')
    if x in options[1:3]:
        run = False

fhand.close()
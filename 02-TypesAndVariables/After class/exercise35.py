import math

circumference = float(input('Enter circumference of tree: '))
diameter = circumference / math.pi

if diameter >= 50:
    print ('Tree can be cut down: True')
elif 0 < diameter < 50:
    print ('Tree can be cut down: False')
else:
    print ('Something went wrong with your circumference')
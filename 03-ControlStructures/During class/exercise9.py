num = input('Enter the number of tasks you have in your test: ')

try:
    num_tasks = int(num)
except:
    print('Enter only integer numbers')
    quit()

completed = input('Enter the number of tasks you have complited: ')

try:
    completed_num = int(completed)
except:
    print('Enter only integer numbers')
    quit()

percentage_number = num_tasks * 0.5
if completed_num >= percentage_number:
    print('Test passed')
else:
    print('Test failed')
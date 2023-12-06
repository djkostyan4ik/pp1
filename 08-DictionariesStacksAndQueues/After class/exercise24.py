import stack

my_number = int(input('Natural number:'))

while my_number != 0:
    stack.push(my_number % 2)
    my_number //= 2

binary = ''

while not stack.empty():
    binary += str(stack.pop())

print('Binary number:',binary)
# all_numbers = []

# attempts = 1
# while attempts > 0:
#     attempts = int(input('Enter number: '))
#     if attempts != 0:
#         all_numbers.append(attempts)
# quantity = len(all_numbers)
# sum = 0
# for i in range (0, len(all_numbers)):
#     sum += all_numbers[i]
#     mean = int(sum / quantity)
# print(f'RESULT: Quantity = {quantity}, Sum = {sum}, Mean = {mean}')





sum = 0
iterations = 0
while True:
    num = int(input('Enter number: '))
    sum +=num
    iterations +=1
    if num == 0:
        break


mean = sum /(iterations - 1)
print(f'RESULT: Quantity = {iterations-1}, Sum = {sum}, Mean = {mean}')
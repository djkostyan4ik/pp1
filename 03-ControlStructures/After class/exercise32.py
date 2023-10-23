first_question = input('Are you interested in computer science? (Y/N): ')
second_question = input('Do you like playing computer games? (Y/N): ')
third_question = input('Do you have an Instagram account? (Y/N): ')
if first_question == 'Y':
    first_question = True
    answer1 = 'Yes'
else:
    first_question = False
    answer1 = 'No'


if second_question == 'Y':
    second_question = True
    answer2 = 'Yes'
else:
    second_question = False
    answer2 = 'No'


if third_question == 'Y':
    third_question == True
    answer3 = 'Yes'
else:
    third_question == False
    answer3 = 'No'


print(f'Interested in computer science: {answer1}')
print(f'Playing computer games: {answer2}')
print(f'Has an Instagram account: {answer3}')
article_number = str(input('Enter EAN-13 article number: '))
amount_of_numbers = len(article_number)
firts_numbers = article_number[0:3]

if  amount_of_numbers== 13:
    print('Article number is correct')
else:
    print('Article number is not correct')

if firts_numbers == '590':
    print('Article manufactured in Poland')
else:
    print('Article manufactured not in Poland')
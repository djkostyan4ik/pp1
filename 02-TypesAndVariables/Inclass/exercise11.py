fathers_inc = int (input ('Enter fathers income: '))

mothers_inc = int (input ('Enter mothers income: '))

num_of_members = int (input ('Enter number of people in family '))


sum = fathers_inc + mothers_inc

total_income = ('Total income: {0}')

print (total_income.format(sum))

one_person_inc = (fathers_inc + mothers_inc) / num_of_members

inc_per_person = ('Income per person: {0}')

print (inc_per_person.format(one_person_inc))

first_person = str(input('Enter first person name: '))
first_person_age = int(input('Enter first person age: '))
second_person = str(input('Enter second person name: '))
second_person_age = int(input('Enter second person age: '))

if first_person_age >= 18 and second_person_age >= 18:
    print(f'Both {first_person} and {second_person}  are adults')

elif first_person_age >= 18 and second_person_age <= 18:
    print(f'Only {first_person} is adult')

elif first_person_age <= 18 and second_person_age >= 18:
    print(f'Only {second_person} is adult')

elif 0 <= first_person_age <= 18 and 0 <= second_person_age <= 18:
    print(f'Nither {first_person} nor {second_person} are adults')

else:
    print('Something went wrong with the age')
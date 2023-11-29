person = {
    'name': 'Marek',
    'surname': 'Banach',
    'age': 25,
    'hobby': ['swimming','excursions'],
    'married': True,
    'phone': {'ladline': '123444321', 'mobile': '777888999'}
}

# a
print('Contents: ',person)
print()
# b
name = person.get('name')
print('Name: ',name)
print()
# c
hobby = person.get('hobby')
print('Hobby: ',hobby)
print()
# d
person['surname'] = 'Nowak'
surname = person.get('surname')
print(surname)
print()
# e
person['married'] = not person['married']
married = person.get('married')
print(married)
print()
# f
person['gender'] = 'male'
gender = person.get('gender')
print(gender)
print()
# g
person['hobby'] += ['bicycle']
hobby2 = person.get('hobby')
print(hobby2)
print()
# h
person['phone']['work'] = '313131444'
print(person['phone'])
print()
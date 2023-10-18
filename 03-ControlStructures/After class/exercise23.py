dog_age = int(input("Enter the dog's age in human years: "))
dog_year = 0
if dog_age >=2:
    dog_year = 4 * (dog_age - 2) + 2 * 10.5
    dog_year = int(dog_year)
elif dog_age < 0:
    print('You need to wright the right age')
else:
    dog_year = dog_age * 10.5

print(f"The dog's age in dpg's years is {dog_year} years.")
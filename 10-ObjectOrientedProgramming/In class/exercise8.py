class Phone():
    def __init__(self,model,producer,prod_year):
        self.model = model
        self.producer = producer
        self.prod_year = prod_year
        self.amount_of_apps_on = 4
        self.is_on = False
    def power_on(self):
        self.is_on = True
    def power_off(self):
        self.is_on = False
    def change_amout_apps_on(self, number):
        self.amout_of_apps_on = number

telefon = Phone(
    'Iphone XS','Apple', '2018')

print(f'My current phone is {telefon.model}, ', end = '')
print(f'produced by company whose name is {telefon.producer}. ', end = '')
print(f'This phone was produced in {telefon.prod_year}.')

telefon.power_on()
telefon.change_amout_apps_on(6)

if telefon.is_on:
    print(f'I am using my phone at the moment.')
else:
    print('I am not using my phone at the moment.')
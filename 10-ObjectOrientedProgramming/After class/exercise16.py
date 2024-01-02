class Cellphone():
    def __init__(self, model, producer, prod_year):
        self.model = model
        self.producer = producer
        self.prod_year = prod_year
        self.is_on = True
        self.amount_of_apps_on = 3
    def power_on(self):
        self.is_on = True
    def power_off(self):
        self.is_off = False
    def change_amout_apps_on(self, number):
        self.amount_of_apps_on = number
    def __str__(self):
        return 'Cellphone: ' + self.model + '\n' + 'Producer: ' + self.producer + '\n' + 'Production year: ' + self.prod_year
cellphone = Cellphone(
    'Iphone 15 PRO', 'Apple', '2023'
)
print(cellphone)
cellphone.power_on()
cellphone.change_amout_apps_on(6)

if cellphone.is_on:
    print(f'I am using my phone at the moment.')
else:
    print('I am not using my phone at the moment.')
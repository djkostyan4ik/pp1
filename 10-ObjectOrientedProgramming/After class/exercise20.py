class Account():
    def __init__(self,account_no):
        self.account_no = account_no
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print(f'You have a deposit PLN {amount} successfully.')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds on the account')
        else:
            self.balance -= amount
            print(f'You have withdrawn PLN {amount} successfully.')

    def display(self):
        number = str(self.account_no)
        print('Bank Account No:', end = ' ')
        print(number[:2], end = '')
        for i in range(6):
            print(' ' + number[i*4+2:i*4+6], end = '')
        print()

        bal = int(self.balance)
        r = self.balance - bal
        r = str(r)
        if len(str(bal)) == 1:
            print('Balance: PLN', str(bal) + '.')
        else:
            print('Balance: PLN', str(bal) + '.' + r[2:4] + '. ',end = '')

acc = Account(12345655559090111100007722)

acc.display()
acc.deposit(25.30)
acc.display()
acc.withdraw(31.70)
acc.display()
acc.withdraw(14)
acc.display()
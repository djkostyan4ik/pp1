class C():
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        if self.age < 18:
            return str(self.surname.lower()) + str(self.name[0].lower())+str(self.seniority)
        else:
            return str(self.surname.upper()) + str(self.name[0].upper())+str(self.seniority)
employee = C('Anna','May',17,7)
print(employee)
employee = C('George','Brown',21,4)
print(employee)
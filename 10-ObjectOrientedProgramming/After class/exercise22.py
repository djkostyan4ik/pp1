class Contact():
    def __init__(self,name,email,telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

class Contact_List():
    def __init__(self):
        self.list = []
    
    def add(self,contact):
        self.list.append(contact)

    def display(self):
        for i in self.list:
            print(i.name.ljust(20),i.email.ljust(24),i.telephone)

l = Contact_List()
l.add(Contact("John Brown", "brown@onet.pl", 555234000))
l.add(Contact("Anna May", "am@o2.pl", 232000199))
l.add(Contact("George Small", "smallg@google.pl", 222999100))
l.add(Contact("Paola Big", "bigpaola@poczta.pl", 100200300))
l.display()
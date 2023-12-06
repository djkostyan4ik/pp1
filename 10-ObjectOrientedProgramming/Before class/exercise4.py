# class PartyAnimal:
#    x = 0

#    def party(self) :
#      self.x = self.x + 1
#      print("So far",self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an.party()
# PartyAnimal.party(an)



# class PartyAnimal:
#    x = 0

#    def party(self) :
#      self.x = self.x + 1
#      print("So far",self.x)

# an = PartyAnimal()
# print ("Type", type(an))
# print ("Dir ", dir(an))
# print ("Type", type(an.x))
# print ("Type", type(an.party))




# class PartyAnimal:
#    x = 0

#    def __init__(self):
#      print('I am constructed')

#    def party(self) :
#      self.x = self.x + 1
#      print('So far',self.x)

#    def __del__(self):
#      print('I am destructed', self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains',an)





from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
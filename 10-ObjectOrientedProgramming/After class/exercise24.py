class C():
    def __init__(self,coordinate_list):
        self.coordinate_list = coordinate_list
        print(coordinate_list)
    def m(self,n):
        coordinates = self.coordinate_list[n-1]
        self.x = coordinates[0]
        self.y = coordinates[1]
        if self.x > 0 and self.y > 0:
            return True
        else:
            return False

coord = C([[2,3],[1,8],[-6,4],[3,-7]])

print(coord.m(2))
print(coord.m(3))

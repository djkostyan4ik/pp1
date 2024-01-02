class Statistics():
    def __init__(self, initial_set = []):
        self.set = initial_set

    def sort(self):
        self.set.sort()

    def len(self):
        return len(self.set)
    
    def add(self, number = None):
        if number != None:
            self.set.append(int(number))
        else:
            self.set.appenf(int(input('Ad a number: ')))

    def max(self):
        return max(self.set)
    
    def min(self):
        return min(self.set)
    
    def median(self):
        self.sort()
        if self.len() % 2 == 0:
            return (self.set[self.len() // 2 - 1] + self.set[self.len() //2]) / 2
        else:
            return self.set[self.len() // 2]
        
    def mean(self):
        sum = 0
        for i in self.set:
            sum += i
        return sum / self.len()
    
    def display(self):
        self.sort()
        x = ''
        for i in self.set:
            x += str(i) + ','
        x = x.rstrip(', ')
        print(x)

    def calculate(self):
        self.display()
        print(f'Minimum:\t\t{self.min()}\nMaximum:\t\t{self.max()}\nArithmetic Mean:\t{self.mean()}\nMedian:\t\t\t{self.median()}')
        

stat = Statistics([12,37,6,9])
stat.add(17)
stat.calculate()
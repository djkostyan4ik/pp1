
def f(mnumbers):
    arr = ['1','2','3','4','5','6','7','a','b','c','d','A','B','C','D']
    counter = 0
    count = 0
    
    for number in mnumbers:
        if number[0] == ('+') or number[0] == ('-'):
            counter += 1
        for char in number:
            if char in arr:
                counter += 1
        if counter == len(number):
            count += 1
        counter = 0
    return count

def main():
    print(f(["A15","-31","7abC","+D1","-gH"]))
    print(f(["A05","-3+1","7ab8C","+D1","-22k"]))
        
if __name__ == '__main__':
    main()

def f(arr2D):
    result = 0
    amount = []
    for row in arr2D:
        people = row[0]-row[1]
        amount.append(people)
    for elem in amount:
        result += int(elem)
    return result

if __name__ == '__main__':
    print(f([[3,0],[6,1]]))
    print(f([[5,4],[6,0]]))
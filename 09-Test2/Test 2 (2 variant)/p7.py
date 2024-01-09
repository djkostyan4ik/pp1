def f(subjects):
    sum = 0
    arr = []
    for key in subjects:
        for val in subjects[key]:
            sum += val
        average = sum/len(subjects[key])
        sum = 0
        arr.append(average)
    maximum = arr.index(max(arr))
    value = list(subjects.items())[maximum]
    for elements in value:
        return elements





if __name__ == '__main__':
    print(f({'math':[3,4,4],
             'geo':[5,4,4,4],
             'comp':[5,4]}))
    
def f(d):
    sum = 0
    count = 0
    values = d.values()
    for num in values:
        sum += num
    average = sum/len(values)
    for value in values:
        if value >= average:
            count += 1
    return count
def main():
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))

if __name__ == '__main__':
    main()
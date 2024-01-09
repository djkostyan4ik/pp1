def f(arr2D):
    for row in arr2D:
        first_col = row[0]
        last_col = row[-1]
        row[0] = last_col
        row[-1] = first_col
    return arr2D

def main():
    print(f([[1,2],[3,4]]))
    print(f([[1,2,3,4],[5,6,7,8]]))

if __name__ == '__main__':
    main()
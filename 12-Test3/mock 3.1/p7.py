def f(arr2D):
    column_sums = {}
    for row in arr2D:
        for index, value in enumerate(row):
            if index in column_sums:
                column_sums[index] += value
            else:
                column_sums[index] = value
    for sum_val in column_sums.values():
        if list(column_sums.values()).count(sum_val) >= 2:
            return True
    return False

def main():
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]]))
    print(f([[3,4],[5,1],[4,7]]))
    print(f([[3,4],[5,9],[4,7]]))

    
if __name__ == '__main__':
    main()

        

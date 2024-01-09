def f(array2D):
    sum_in_col = 0
    sum_in_row = 0
    for row in array2D:
        sum_in_col += row[0]

    for elem in array2D[0]:
            sum_in_row += elem
            
    
    if sum_in_row == sum_in_col:
        return True
    else:
        return False



if __name__ == '__main__':
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))
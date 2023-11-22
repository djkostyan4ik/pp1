# i = 1
# j = 1

# for row in arr:
#     for elem in row:
#         arr[arr.index(row)][row.index(elem)] += i
#         i += j
#     for i in range(j+1):
#         i += 1
#     j += 1

# print(*arr)

twoD_arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def display_arr(array):

    # find how long are numbers in the array
    max_array = []

    for i in range(len(array)):
        max_array.append(max(array[i]))
    
    max_max = len(str(max(max_array)))

    # prepare string for displaying the array
    x = ""

    for i in range(len(array)):
        for j in range(len(array[i])):
            x += str(twoD_arr[i][j]).rjust(max_max)
            if j != len(array[i]) - 1:
                x += " "
            else:
                x += "\n"
    
    return x


for i in range(len(twoD_arr)):
    for j in range(len(twoD_arr[0])):
        twoD_arr[i][j] = (i + 1) * (j + 1)

print(display_arr(twoD_arr))
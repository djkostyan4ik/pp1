arr = [2, 3, 7, 5, 4]
middle_value = arr[int(len(arr)/2)]
print("Array: ", arr)
print("No. of elements: ", len(arr))
print("First value: ", arr[0])
print("Second value: ", arr[1])
print("Last value: ", arr[-1])
print("Last but one value: ", arr[4])
print("Sum of the first and last value: ", arr[0]+arr[4])
print("Middle vale: ", middle_value)
k = ''
for i in arr:
    k += str(i) + ' '
print(k)
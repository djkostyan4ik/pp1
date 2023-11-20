arr = ["Genowefa", "Onufry", "Celestyna", "Anojzy", "Pankracy"]
result = arr[0]
for element in arr:
    if len(element) > len(result):
        result = element
print ("Names: ", *arr)
print("Longest name: ", result)
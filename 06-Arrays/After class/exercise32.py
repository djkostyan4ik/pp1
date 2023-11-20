number = int(input("Number: "))
input_list = input("Array: ")
array = input_list.split()
def occurs(number, array):
    if str(number) in array:
        result = f"Number {number} appears in the array"
        # return True
    elif str(number) not in array:
        result = f"Number {number} is not in the array"
        # return False
    return result
        
if __name__ == "__main__":
    print("Result:",occurs(number, array))
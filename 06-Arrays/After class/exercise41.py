def issubset(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if (arr1[i]==arr2[j]):
                break
        if (arr1[i] != arr2[j]):
            return False
        if (j == len(arr2)):
            return False
    return True
 
if __name__ == "__main__":

    arr1 = [11, 3, 7]
    arr2 = [1, 2, 6]
 
    if(issubset(arr1, arr2)):
        print("arr1[] is subset of arr2[] ")
    else:
        print("arr1[] is not a subset of arr2[]")
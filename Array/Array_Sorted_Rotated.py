def Arrayis_Sorted_Rotated(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:  
            count += 1

        if count > 1:
            return False
    return True

arr1 = [3, 4, 5, 1, 2]  
arr2 = [2, 1, 3, 4]     
arr3 = [1, 2, 3]        

print("Array 1 is sorted and rotated:", Arrayis_Sorted_Rotated(arr1))
print("Array 2 is sorted and rotated:", Arrayis_Sorted_Rotated(arr2))
print("Array 3 is sorted and rotated:", Arrayis_Sorted_Rotated(arr3))

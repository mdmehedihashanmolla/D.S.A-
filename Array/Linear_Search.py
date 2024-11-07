def Linear_Search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return f"Value Found {num} in the list"
    return -1  
l = [5, 5, 36, 9, 1, 2, 3]
num = 100
print(Linear_Search(l, num))

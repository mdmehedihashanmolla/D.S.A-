def Left_Rotate_Array(arr, n):
    temp = arr[0]  # Store the first element in a temporary variable
    for i in range(1, n):
        arr[i - 1] = arr[i]  # Shift elements to the left
    arr[n - 1] = temp  # Move the first element to the last position
    return arr
l = [1, 2, 3, 4, 5]
n = len(l)
print(Left_Rotate_Array(l, n))

def rotate_to_right(arr, n, k):
    if n == 0:
        return
    k = k % n  # Handle cases where k is larger than n

    # Step 1: Store the last k elements in a temporary array
    temp = arr[-k:]  # This will store the last k elements

    # Step 2: Shift the remaining elements to the right
    for i in range(n - k - 1, -1, -1):
        arr[i + k] = arr[i]

    # Step 3: Copy the k elements from temp to the start of the array
    for i in range(k):
        arr[i] = temp[i]

n = 7
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate_to_right(arr, n, k)
print("After rotating the elements to the right:")
print(arr)

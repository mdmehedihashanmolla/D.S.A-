def Largest_Element(arr, n):
    max = arr[0]
    for i in range(0, n, 1):
        if (max <arr[i]):
            max = arr[i]
    return max

lst = [45,36,798,65]
n = len(lst)
print(Largest_Element( lst, n))
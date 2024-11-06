import sys
def Find_SecondSmallestElement(arr,n):
    if n<2:
        return -1
    
    small = sys.maxsize
    second_small = sys.maxsize

    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
    return second_small

def Find_SecondLargestElement(arr, n):
    if n<2:
        return -1
    large = -sys.maxsize
    second_large = -sys.maxsize
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]

        elif arr[i]> second_large and arr[i] != large:
            second_large = arr[i]
    return second_large

arr = [4,6,9,2,3,7]
n = len(arr)
SecondSmall = Find_SecondSmallestElement(arr,n)
SecondLarge = Find_SecondLargestElement(arr,n)

print("Second Smallest value in the array is ", SecondSmall)
print("Second Largest Value in the array is : ", SecondLarge)
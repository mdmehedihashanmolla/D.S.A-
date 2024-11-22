def move_Zero_end(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:

            nums[i], nums[j]  = nums[j], nums[i]
            j += 1

    return nums

arr = [1,2,3,4,0,0,0,45,64]
print("Array after moving zeros to the end ")
print(move_Zero_end(arr))
# Pivot Index

def pivotIndex(nums):
    pointer = 0
    while pointer < len(nums):
        if (sum(nums[:pointer]) == sum(nums[pointer+1:])):
            return pointer
        pointer += 1
    return -1
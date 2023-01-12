#=============================
# Remove value
# By Wasam
#=============================

def removeElement(nums, val):
    ind = 0
    while ind < len(nums):
        if nums[ind] == val:
            nums.pop(ind)
        else:
            ind += 1
    count = len(nums)
    return count, nums
#=============================
# InPlace Sort
# By Wasam
#=============================

def removeDuplicates(nums):
    ind = 0
    while ind < len(nums) -1:
        if nums[ind] == nums[ind+1]:
            nums.pop(ind)
        else:
            ind += 1
    count = len(nums)
    return count, nums
#=============================
# Search Insert Position
# By Wasam
#=============================

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        ind = 0
        while ind < len(nums):
            if target < nums[ind]:
                break
            else:
                ind += 1
        return ind
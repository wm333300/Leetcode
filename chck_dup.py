#=============================
# check_dp
# By Wasam
#=============================

        
def containsDuplicate(nums):
    nums.sort()
    ind = 0
    while ind < len(nums)-1:
        if nums[ind] == nums[ind+1]: return True
        ind += 1
    return False

def containsNearbyDuplicate(nums, k):
    ind = 0
    tracker = 0
    i = 0
    j = 0
    if len(nums) == 1: return False
    while ind < len(nums)-1:
        tracker = nums[ind]
        if tracker in nums[ind+1:]:
            i = ind
            j = nums[ind+1:].index(tracker) + len(nums[:ind+1]) 
            if abs(i-j) <= k:
                break
            ind += 1
        ind += 1
    if (i == 0) and (j == 0): return False
    return abs(i-j) <= k
#++++++++++++++++++++++++++++++++++
# cbs
# Wasam
#++++++++++++++++++++++++++++++++++

def pivotIndex(nums):
    ind = 0
    leftsum = 0
    rightsum = 0
    curr_pivot = -1
    if len(nums) == 0: return curr_pivot
    if len(nums) == 1: return 0
    while ind < len(nums):
        if (ind == 0): 
            rightsum = sum(nums[ind+1:])
            if rightsum == 0: 
                curr_pivot = ind
                break
            else:
                ind += 1
        elif (ind == (len(nums)-1)):
            leftsum = sum(nums[:ind])
            if leftsum == 0:
                curr_pivot = ind
                break
            else:
                ind += 1
        else:
            rightsum = sum(nums[ind+1:])
            leftsum = sum(nums[:ind])
            print(rightsum, leftsum, ind, nums[ind+1:], nums[:ind])
            if rightsum == leftsum:
                curr_pivot = ind
                break
            else:
                ind += 1
    return curr_pivot
        
        
        
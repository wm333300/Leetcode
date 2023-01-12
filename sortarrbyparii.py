#++++++++++++++++++++++++++++++++++
# sabpii
# Wasam
#++++++++++++++++++++++++++++++++++

def sortArrayByParityII(nums):
    ind = 0
    while ind < len(nums):
        if ((ind % 2 == 1 and nums[ind] % 2 == 0) or 
            (ind%2 == 0 and nums[ind] % 2 == 1)):
            x = nums[ind]
            del nums[ind]
            nums.append(x)
            ind = 0
        else:
            ind += 1
    return nums
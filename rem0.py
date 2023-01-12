#=============================
# firstUniqChar
# By Wasam
#=============================

def moveZeroes(nums):   
    count = nums.count(0)
    nums = list(filter(lambda x: x != 0, nums))
    print(nums)
    ind = 0
    while ind < count:
        nums.append(0)
        ind += 1
    return nums
        
            
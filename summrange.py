#=============================
# summaryRanges
# By Wasam
#=============================

def summaryRanges(nums):
    ind = 0
    curr = []
    ans = []
    while ind < len(nums)-1:
        if ind == len(nums) - 2:
            if nums[ind+1] == nums[ind]+1:
                curr.append(nums[ind:])
                ans.append("{0}->{1}".format(curr[0],curr[1]))
                curr = []
                ind += 1
            else:
                curr.append(nums[ind])
                ans.append("{}".format(nums[ind]))
                
        if nums[ind+1] == nums[ind]+1:
            curr.append(nums[ind])
            ind += 1
        if nums[ind+1] > nums[ind]:
            curr.append(nums[ind])
            ind += 1
        ans.append(curr)
        ind += 1
    return ans
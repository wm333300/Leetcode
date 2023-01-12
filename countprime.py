#++++++++++++++++++++++++++++++++++
# maxcon
# Wasam
#++++++++++++++++++++++++++++++++++

def findMaxConsecutiveOnes(nums):
    ind1 = 0
    counts_list = []
    while ind1 < len(nums):
        ind2 = ind1
        count = 0
        while ind2 < len(nums):
            if nums[ind2] == 1:
                count += 1
                ind2 += 1
            elif nums[ind2] == 0:
                break
            else:
                ind2 += 1
        counts_list.append(count)
        ind1 += 1
    return max(counts_list)

def findMaxConsecutiveOnes_2(nums):
    ind = 0
    count = 0
    counts_list = []
    while ind < len(nums):
        if nums[ind] == 1:
            count += 1
            ind += 1
        elif nums[ind] == 0:
            counts_list.append(count)
            count = 0
            ind += 1
        else:
            ind += 1
    counts_list.append(count)
    return max(counts_list)
            
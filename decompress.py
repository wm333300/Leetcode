#++++++++++++++++++++++++++++++++++
# decompressRLElist
# Wasam
#++++++++++++++++++++++++++++++++++

def decompressRLElist(nums):
    cr_subs = [nums[elem:elem+2] for elem in range(0,len(nums)-1,2)]
    ans = []
    for elem in cr_subs:
        ind = 0
        while ind < elem[0]:
            ans.append(elem[1])
            ind += 1
    return ans
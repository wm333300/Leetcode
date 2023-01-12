#=============================
# msa()
# By Wasam
#=============================

def msa(nums1, m, nums2, n):
    ind = 0
    while ind < n:
        nums1.pop(ind+m)
        nums1.insert(ind+m, nums2[ind])
        ind += 1
    nums1.sort()
    return nums1
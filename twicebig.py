#++++++++++++++++++++++++++++++++++
# domnum
# Wasam
#++++++++++++++++++++++++++++++++++

def dominantIndex(nums):
    large = max(nums)
    check = []
    index = []
    for elem in nums:
        if elem != large:
            if large >= (elem *2):
                check.append(True)
                index.append(0)
            else:
                index.append(0)
                check.append(False)
        else:
            index.append("this")
    if all(check):
        return index.index("this")
    else:
        return -1
                
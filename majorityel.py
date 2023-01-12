#=============================
# Remove dupes
# By Wasam
#=============================

def maj_el(nums):
    def removedup(nums_0):
        ind = 0
        while ind < len(nums_0)-1:
            if nums_0[ind] == nums_0[ind+1]:
                nums_0.pop(ind)
            else:
                ind += 1
        count = len(nums_0)
        return nums_0
    nums.sort()
    main_nums = nums.copy()
    checker = removedup(nums)
    counts = []
    for elem in checker:
        counts.append(main_nums.count(elem))
    return checker[counts.index(max(counts))]
        
        
def maj_el_eff(nums):
    curr_high = nums[0]
    curr_h_count = {}
    ind = 0
    nums.sort()
    while ind < len(nums):
        if nums[ind] == curr_high:
            if curr_high not in curr_h_count: 
                curr_h_count[curr_high] = 1
                ind += 1
            curr_h_count[curr_high] += 1
            ind += 1
        if nums[ind] > curr_high:
            curr_high = nums[ind]
            curr_h_count[curr_high] = 1
            ind += 1
        if nums[ind] < curr_high:
            ind += 1
    return curr_h_count
    
    
# Guess

def guess(p, corr_p):
    if p > corr_p: return -1
    elif p < corr_p: return 1
    else: return 0

def guessNumber(n, pick):
    if n==1: return 1
    start = 0
    mid = n//2
    end = n
    picker = -2
    while picker != 0:
        picker = guess(mid, pick)
        if ((mid == n-1) and (picker == 1)):return n
        elif picker == -1:
            end = mid
            mid = end//2
        else:
            start = mid
            mid = start+((end-start)//2)
    return start
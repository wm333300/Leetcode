#++++++++++++++++++++++++++++++++++
# setbits
# Wasam
#++++++++++++++++++++++++++++++++++

def relativeranks(score):
    ans_d = {}
    ans = []
    score_sort = [el for el in score]
    score_sort.sort()
    ind = len(score)-1
    while ind >= 0:
        if score[ind] == max(score):
            ans_d[score[ind]] = "Gold Medal"
            ind -= 1
        elif score[ind] == score_sort[len(score_sort)-2]:
            ans_d[score[ind]] = "Silver Medal"
            ind -= 1
        elif score[ind] == score_sort[len(score_sort)-3]:
            ans_d[score[ind]] = "Bronze Medal"        
            ind -= 1
        else:
            ans_d[score[ind]] = str(ind+1)
            ind -= 1
    for elem in score:
        ans.append(ans_d[elem])
    return ans

def relative_ranks_2(score):
    ans_d = {}
    ans = []
    score_sort = score[:]
    score_sort.sort()
    score_sort.reverse()
    print(score_sort)
    for elem in range(len(score_sort)):
        if elem == 0:
            ans_d[score_sort[elem]] = "Gold Medal"
        elif elem == 1:
            ans_d[score_sort[elem]] = "Silver Medal"
        elif elem == 2:
            ans_d[score_sort[elem]] = "Bronze Medal" 
        else:
            ans_d[score_sort[elem]] = str(elem+1)
    ans = [ans_d[elem] for elem in score]
    return ans
        
  
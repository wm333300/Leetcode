#=============================
# Pascal's Triangle
# By Wasam
#=============================

def pt(numRows):
    
    def list_sum(li):
        ind = 0
        ans = []
        while ind < len(li)-1:
            ans.append(sum(li[ind:ind+2]))
            ind += 1
        return ans   
    
    ind = 0
    answer = []
    while ind < numRows:    
        if ind == 0:
            answer.append([1])
            ind += 1
        elif ind == 1:
            answer.append([1,1])
            ind += 1
        else:
            answer.append([1] + list_sum(answer[ind-1]) + [1])
            ind += 1
    return answer
            


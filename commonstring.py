#=============================
# Common String
# By Wasam
#=============================



def longestCommonPrefix(strs):
    
    ind1 = 0
    trash = []
    corr = []
    count = 0
    
    def allequal(los):
        question = False
        ind_0 = 0
        while (ind_0 < len(los)):
            if (ind_0 == (len(los)-2)):
                if los[ind_0] == los[ind_0+1]:
                    question = True
                    ind_0 += 1
                else:
                    question = False
                    return question
            elif (ind_0 == len(los)-1):
                return question
            else:
                if (los[ind_0] == los[ind_0+1]):
                    question = True
                    ind_0 += 1
                else:
                    question = False
                    return question       
                    
    while (ind1 < len(strs)):
        checker = allequal(strs)
        if checker:
            corr = strs[ind1]
            ind1 += len(strs)
        else:
            ind2 = 0
            while (ind2 < len(strs[ind1])):
                ind3 = 0
                while (ind3 < len(strs)):
                    if (strs[ind1][ind2] in strs[ind3]):
                        count += 0
                        ind3 += 1
                    else:
                        count += 1
                        ind3 += 1
                if ((count == 0)):
                    corr.append(strs[ind1][ind2])
                    ind2 += 1
                else:
                    trash.append(strs[ind1][ind2])
                    ind2 += 1
            ind1 += 1
    corr = "".join(corr)
    return corr,count
         
            
def longestCommonPrefix_1(strs):
    
    check = False
    corr = []
    ind1 = 0
    min_of_strs = min(map(len, strs))
    
    if (len(strs) == 1): return strs[0]
    
    while (ind1 < min_of_strs):
        ind2 = 0
        while (ind2 < len(strs)-1):
            if (strs[0][ind1] == strs[ind2+1][ind1]):
                check = True
                ind2 += 1
            else:
                check = False
                ind2 += 1
        if (check): corr.append(strs[0][ind1])
        else: break
        ind1 += 1
    corr = "".join(corr)
    return corr


                
            
#++++++++++++++++++++++++++++++++++
# LKF
# Wasam
#++++++++++++++++++++++++++++++++++

def licenseKeyFormatting(s, k):
    char_list = [elem.upper() for elem in s if (elem.isalnum() and (elem != "-"))]
    curr = ""
    ans = []
    #print(char_list)
    start = 0
    if (len(s[start:s.index("-")]) < k):
        ans.append(curr.join(char_list[start:s.index("-")]))
        start+=1
    ans.extend([curr.join(char_list[elem:k+elem]) for elem in range(start,(len(char_list)),k)])
    #ans = [curr.join(char_list[elem:s.index("-")]) if ((len(s[elem:s.index("-")]) < k) and elem == 0) else curr.join(char_list[elem:k+elem]) for elem in range(0,(len(char_list)),k)]
    ans_str = "-".join(ans)
    return ans_str

def licenseKeyFormatting_2(s, k):
    char_list = [elem.upper() for elem in s if (elem.isalnum() and (elem != "-"))]
    char_list.reverse()
    
    rem = len(char_list) % k
    curr = ""
    ans = []
    if rem == 0 or rem == 2:
        ans = [curr.join(char_list[elem:k+elem]) for elem in range(0,(len(char_list)),k)]
    else:
        start = 0
        if (len(s[start:s.index("-")]) < k):
            ans.append(curr.join(char_list[start:s.index("-")]))
            start+=1
        ans.extend([curr.join(char_list[elem:k+elem]) for elem in range(start,(len(char_list)),k)])         
    ans_str = "-".join(ans)
    return ans_str


def licenseKeyFormatting_3(s, k):
    char_list = [elem.upper() for elem in s if (elem.isalnum() and (elem != "-"))]
    char_list.reverse()
    curr = ""
    ans = [curr.join(char_list[elem:k+elem]) for elem in range(0,(len(char_list)),k)]
    ans_str = "-".join(ans)
    return ans_str[::-1]
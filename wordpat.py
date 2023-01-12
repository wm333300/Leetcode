#++++++++++++++++++++++++++++++++++
# wordpat
# Wasam
#++++++++++++++++++++++++++++++++++

def wordPattern(pattern, s):
     """
     :type pattern: str
     :type s: str
     :rtype: bool
     """
     def rem_dups(st):
          ind = 0
          ans = []
          while ind < len(st):
               if st[ind] not in st[ind+1:]:
                    ans.append(st[ind])
                    ind += 1
               else:
                    ind += 1
          ans.reverse()
          return ans     
     strl = s.split(" ")
     pat_1 = rem_dups(pattern)
     strl_1 = rem_dups(strl)
     #d = {}
     #print(pat_1, strl_1)
     for elem in range(len(pat_1)):
          d[pat_1[elem]] = strl[elem] 
     ans = []
     for elem in pattern:
          ans.append(d[elem])  
     return ans == strl

def wordPattern_1(pattern, s):
     pat_1 = [elem for elem in pattern]
     str_1 = s.split(" ")
     d = {}
     for elem in range(len(pat_1)):
          d[pat_1[elem]] = []
     for elem in range(len(pat_1)):
          if str_1[elem] not in d[pat_1[elem]]:
               d[pat_1[elem]].append(str_1[elem])     
     for elem in d:
          if len(d[elem]) > 1:
               return False
     return True
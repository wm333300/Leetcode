#++++++++++++++++++++++++++++++++++
# My Queue
# Wasam
#++++++++++++++++++++++++++++++++++

class ListNode(object):
     def __init__(self, val, next=None):
          self.val = val
          self.next = next

def ll_gen(alst):
     alst.reverse()
     head = ListNode(alst[0])
     for elem in alst[1:]:
          head = ListNode(elem, head)
     return head


def isPalindrome(head):
     ans = []
     comp_s = []
     init_s = []
     while head != None:
          ans.append(head.val)
          head = head.next
     if len(ans) %2 ==1:
          init_s = ans[:len(ans)//2]
          comp_s = ans[(len(ans)//2)+2:]
     if len(ans) %2 ==0:
          init_s = ans[:len(ans)//2]
          comp_s = ans[(len(ans)//2):] 
     comp_s.reverse()     
     print(init_s, comp_s)
     return init_s == comp_s
     

t1 = ll_gen([1,2,2,1])
t2 = ll_gen([1,2])
t3 = ll_gen([1])
t4 = ll_gen([1,1,2,1])
               
               


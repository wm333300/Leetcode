#++++++++++++++++++++++++++++++++++
# Linked List Cycle
# Wasam
#++++++++++++++++++++++++++++++++++

class ListNode(object):
         def __init__(self, x):
                  self.val = x
                  self.next = None

def ll_gen(ll):
         ans = ListNode(0)
         for elem in ll:
                  ans.val = elem
                  print(ans.val)
                  ans.next = ans
         return ans

def hasCycle(head):
         stack = []
         pos = -1
         while head.val not in stack:
                  if head.next == None:
                           break
                  else:
                           stack.append(head.val)
                           head = head.next
         return stack

x = 1
ll = [1,2,3,x,4]
mp = list(map(lambda y: x is y, ll))

#=============================
# revlinkedlist
# By Wasam
#=============================

class ListNode(object):
     def __init__(self, val, next):
          self.val = val
          self.next = next
  

def list_make(node):
     ans = []
     while node != None:
          ans.append(node.val)
          node = node.next
     return ans

def ll_make(alst):
     i = 0
     next_node = ListNode(alst[0], None)
     while i < len(alst):
          if i == len(alst)-1:
               next_node.val = alst[i]
               i += 1
          else:
               next_node.val = alst[i]
               next_node = ListNode(next_node.val, next_node)
               i += 1
     return next_node

def ll_makerec(alst, node):
     if alst == []:
          return None
     x = ll_makerec(alst[1:], node)
     return ListNode(alst[0], x)

def revlinkedlists(head):
     pass
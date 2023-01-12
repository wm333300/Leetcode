#+++++++++++++++++++++++++++++++++
# ll
# Wasam Syed
#+++++++++++++++++++++++++++++++++

class ListNode(object):
     def __init__(self, x, next):
          self.val = x
          self.next = next
     def __repr__(self):
          ans = []
          while self != None:
               ans.append(self.val)
               self = self.next
          return str(ans)

def deleteNode(s, node):
     tracker = s
     while tracker.next != None:
          if tracker.next.val == node:
               tracker.next = tracker.next.next
          tracker = tracker.next
          if tracker == None:
               break

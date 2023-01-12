#=============================
# remdup()
# By Wasam
#=============================

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def ll_to_l(ll):
    ans = []
    while ll != None:
        ans.append(ll.val)
        ll = ll.next
    return ans

def l_dup_rem(l):
    ind = 0
    while ind < len(l) -1:
        if l[ind] == l[ind+1]:
            l.pop(ind)
        else:
            ind += 1
    return l       

def ll_make(l):
    ind = len(l) - 1
    next_node = None
    while ind >= 0:
        next_node = ListNode(l[ind], next_node)
        ind -= 1
    return next_node

def deleteDuplicates(head):
    pass
        
        
        
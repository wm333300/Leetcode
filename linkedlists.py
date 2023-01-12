#=============================
# Linked Lists
# By Wasam
#=============================

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, nexti=None):
        self.val = val
        self.nexti = nexti

def list_length(l):
    count = 0
    while l != None:
        count+=1
        l = l.nexti
    return count

def llmerge(l1, l2):
    next_node = None
    leng_1 = list_length(l1)
    count = leng_1 - 1
    tracker = l1.val
    while count >= 0:
        if tracker >= l2.val:
            tracker = l1.val
            next_node = ListNode(l2.val, next_node)
            count -= 1
        elif tracker < l2.val:
            tracker = l2.val
            next_node = ListNode(l1.val, next_node)
            count -= 1
        else:
            next_node = ListNode(tracker, next_node)
            count -= 1
    return next_node
            
    
        
            
        
        

    
def list_traverse(l):
    ans = []
    while l != None:
        ans.append(l.val)
        l = l.nexti
    return ans

def llmerge_2(l1, l2):
    lst_1 = []
    lst_2 = []
    ans = []
    
    
    while l1 != None:
        lst_1.append(l1.val)
        l1 = l1.nexti
        
    while l2 != None:
        lst_2.append(l2.val)
        l2 = l2.nexti
    ans += lst_1 + lst_2
    ans.sort()
    
    i = 0
    next_node = None
    while i
    
def list_reverse(l):
    while l != None:
        print(l.val)
        l = l.nexti

def list_rev_rec_pr(l):
    if l == None:
        return
    else:
        list_rev_rec(l.nexti)
        print(l.val)

def list_mid(l):
    leng = list_length(l)
    stop = leng // 2
    track = 0
    while track != stop:
        track += 1
        l = l.nexti
    return l.val

def list_make(li, n = 0):
    if n == len(li) -1:
        return ListNode(li[n])
    else:
        return ListNode(li[n], list_make(li, n + 1))

def list_make_it(li):
    i = len(li) - 1
    next_node = None
    while i >= 0:
      # we can create the node here
        next_node = ListNode(li[i], next_node)
        i-=1
    return next_node

def list_make_it_2(li, li_2):
    i = len(li) - 1
    next_node = None
    while i >= 0:
      # we can create the node here
        if li[i] >= li_2[i]:
            next_node = ListNode(li_2[i], next_node)
            i-=1
        else:
            next_node = ListNode(li[i], next_node)
            i-=1            
    return next_node



def list_make_jan(li):
    if len(li) == 0:
        return None
      
    val = li[0]
    return ListNode(val, list_make_jan(li[1:]))
        
def list_make_2(v, n):
    ans = ListNode(v, n) 
    return ans

def list_make_3(li):
    ind = 0
    next_node = None
    while ind < len(li):
        next_node = ListNode(li[ind], next_node)
        ind += 1
    return next_node

def list_make_rev(l):
    count = 0
    next_node = None
    leng = list_length(l)
    while count < leng:
        next_node = ListNode(l.val, next_node)
        count += 1
    return next_node



    
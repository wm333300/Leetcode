#=============================
# btiot()
# By Wasam
#=============================

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

def preorderTraversal(root):
     stack = [root]
     res = []
     track = root
     while stack != []:
          track = stack.pop()
          if track.left != None: stack.append(track.left)
          if track!= None: res.append(track.val)
          if track.right != None: stack.append(track.right)
     return res
     
# TreeNode(1,None,(TreeNode(2, (TreeNode(3, None, None)), None, None))))


          
def pretrav(root, stack):
     if root == None: 
          return 
     stack.append(root.val)
     intrav(root.left, stack)
     intrav(root.right, stack)
     return(stack)
     
def intrav(root, stack):
     if root == None: 
          return
     intrav(root.left, stack)
     stack.append(root.val)
     intrav(root.right, stack) 
     return(stack)

def posttrav(root, stack):
     if root == None: return 
     intrav(root.left, stack)
     intrav(root.right, stack)
     stack.append(root.val)
     return(stack)

def intravit(root):
     stack = [root]
     res = []
     tracker = root
     while stack != []:
          if tracker == None: break
          if tracker.left != None: 
               tracker = tracker.left
               stack.append(tracker)
          tracker = stack.pop()
          res.append(tracker.val)
          if tracker.right != None:
               tracker = tracker.right
               stack.append(tracker)    
     return res
               
     
def isSymmetric(root):
     """
     :type root: TreeNode
     :rtype: bool
     """
     def intrav(r, stack):
          if r == None: 
               stack.append(-1)
               return
          stack.append(r.val)
          intrav(r.left, stack)
          
          intrav(r.right, stack)
          
          return(stack)
     if root.left == None and root.right == None: return True
     if root.left == None or root.right == None: return False
     a = intrav(root.left, [])

     b = intrav(root.right, [])
     #b.reverse()

     print(a)
     print(b)
          
TC1= TreeNode(1, (TreeNode(2, (TreeNode(3, None, None)), (TreeNode(4, None, None)))), (TreeNode(2, (TreeNode(4, None, None)), (TreeNode(3, None, None)))))
TC2= TreeNode(1, (TreeNode(2, None, (TreeNode(3, None, None))), (TreeNode(2, None, (TreeNode(3, None, None))))))         
TC3= TreeNode(1, (TreeNode(2, (TreeNode(2, None, None)), None)), (TreeNode(2, (TreeNode(2, None, None)), None)))          

def check_symmetry(n1, n2):
     

     
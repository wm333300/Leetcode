#=============================
# issym
# By Wasam
#=============================

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
  


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
          
TC1 = TreeNode(1, (TreeNode(2, (TreeNode(3, None, None)), (TreeNode(4, None, None)))), (TreeNode(2, (TreeNode(4, None, None)), (TreeNode(3, None, None)))))
TC2 = TreeNode(1, (TreeNode(2, None, (TreeNode(3, None, None))), (TreeNode(2, None, (TreeNode(3, None, None))))))         
TC3 = TreeNode(1, (TreeNode(2, (TreeNode(2, None, None)), None)), (TreeNode(2, (TreeNode(2, None, None)), None)))          
TC4 = TreeNode(1,None,(TreeNode(2, (TreeNode(3, None, None)), None)))

def check_symmetry(n1, n2):
     pass
     

     
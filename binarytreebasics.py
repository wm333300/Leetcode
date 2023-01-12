#++++++++++++++++++++++++++++++++++
# binarytreebasics
# Wasam
#++++++++++++++++++++++++++++++++++

class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def depth_first_traversal(bt):
    stack = [bt]
    current = 0
    values = []
    while stack != []:
        current = stack.pop()
        values.append(current.val)
        
        if current.right != None:
            stack.append(current.right)
        if current.left != None:
            stack.append(current.left)
    return values

a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
    
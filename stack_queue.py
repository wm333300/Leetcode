#++++++++++++++++++++++++++++++++++
# Contains nearby duplicate
# Wasam
#++++++++++++++++++++++++++++++++++

class MyStack(object):

    def __init__(self):
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lst.append([x])

    def pop(self):
        """
        :rtype: int
        """
        y = self.lst[-1]
        del self.lst[-1]
        return y

    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.lst == []:
            return True
        else: 
            return False


myStack = MyStack()
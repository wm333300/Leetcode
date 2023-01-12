#++++++++++++++++++++++++++++++++++
# My Queue
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
        y = self.lst[0]
        del self.lst[0]
        return y

    def peek(self):
        """
        :rtype: int
        """
        return self.lst[0]

    def empty(self):
        """
        :rtype: bool
        """
        if self.lst == []:
            return True
        else: 
            return False


myStack = MyStack()
##155.min stack class
# O(1) complexity
# tracking minimum by using min_list that's kept in sync with the normal stack

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_list:
            self.min_list.append(val)
        else:
            if val < self.min_list[-1]:
                self.min_list.append(val)
            else:
                self.min_list.append(self.min_list[-1])

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.min_list.pop()
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
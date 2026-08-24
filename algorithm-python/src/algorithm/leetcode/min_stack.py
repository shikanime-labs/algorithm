class MinStack:
    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, val):
        """
        :type val: int
        :rtype: none
        """
        if not self.min_data or self.min_data[-1] >= val:
            self.min_data.append(val)
        self.data.append(val)

    def pop(self):
        """
        :rtype: none
        """
        if self.min_data[-1] == self.data[-1]:
            self.min_data.pop()
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_data[-1]


# your minstack object will be instantiated and called as such:
# obj = minstack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getmin()

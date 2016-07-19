#coding:utf-8
'''
leetcode: Min Stack
'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # 保存数据的栈
        self.min_stack = [] # 保存最小元素的栈

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            min_value = self.min_stack[len(self.min_stack) - 1] # 当前栈中的最小元素
            # 如果压入栈中的元素比当前栈中的最小元素还小
            if x < min_value:
                self.min_stack.append(x)
            else:
                self.min_stack.append(min_value)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.min_stack[len(self.min_stack) - 1]

        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#coding:utf-8
'''
leetcode: Implement Queue using Stacks
'''

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_1 = [] # 正序存放输入的数据,用于输入数据
        self.stack_2 = [] # 逆序存放输入的数据,用于输出数据

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack_1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return None

        if len(self.stack_2) == 0:
            for i in range(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())

        self.stack_2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        if len(self.stack_2) == 0:
            for i in range(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())

        return self.stack_2[len(self.stack_2) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_1) == 0 and len(self.stack_2) == 0

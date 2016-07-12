#coding:utf-8
'''
leetcode: Implement Stack using Queues
'''


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 需要时刻保持有一个队列为空,来存储出栈时的其他元素
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.queue_1) == 0 and len(self.queue_2) == 0:
            self.queue_1.append(x)
        elif len(self.queue_1) == 0:
            self.queue_2.append(x)
        else:
            self.queue_1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return

        if len(self.queue_1) != 0:
            for i in range(len(self.queue_1) - 1):
                self.queue_2.append(self.queue_1[i])

            self.queue_1 = []
        else:
            for i in range(len(self.queue_2) - 1):
                self.queue_1.append(self.queue_2[i])

            self.queue_2 = []

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        if len(self.queue_1) != 0:
            return self.queue_1[len(self.queue_1) - 1]

        else:
            return self.queue_2[len(self.queue_2) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue_1) == 0 and len(self.queue_2) == 0

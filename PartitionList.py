#coding:gb2312
'''
leetcode: Partition List
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        smaller_num = [] # �洢��xС����
        larger_num = [] # �洢��x�����

        #���δ洢��xС�ͱ�x�����
        temp = head
        while temp:
            if temp.val < x:
                smaller_num.append(temp.val)
            else:
                larger_num.append(temp.val)

            temp = temp.next

        temp = head
        for i in range(len(smaller_num)):
            temp.val = smaller_num[i]
            temp = temp.next

        for i in range(len(larger_num)):
            temp.val = larger_num[i]
            temp = temp.next

        return head


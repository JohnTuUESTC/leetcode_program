#coding:gb2312
'''
leetcode: Rotate List
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or k == 0:
            return head

        list_len = 1

        temp_node = head
        while temp_node.next != None:
            list_len += 1
            temp_node = temp_node.next

        temp_node.next = head

        k %= list_len

        # 将head移动到新头结点的前一个结点
        for i in range(list_len - k, 1, -1):
            head = head.next
            list_len -= 1

        new_head = head.next
        head.next = None

        return new_head


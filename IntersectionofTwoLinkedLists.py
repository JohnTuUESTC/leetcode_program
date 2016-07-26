#coding:utf-8
'''
leetcode: Intersection of Two Linked Lists
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None

        len_A = self.List_Len(headA)
        len_B = self.List_Len(headB)

        node_A = headA
        node_B = headB

        if len_A > len_B:
            num = 0
            while num < len_A - len_B:
                node_A = node_A.next
                num += 1
        elif len_A < len_B:
            num = 0
            while num < len_B - len_A:
                node_B = node_B.next
                num += 1

        while node_A:
            if node_A == node_B:
                return node_A

            node_A = node_A.next
            node_B = node_B.next

        return None

    # 计算链表的长度
    def List_Len(self, head):
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        return length

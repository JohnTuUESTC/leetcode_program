#coding:utf-8
'''
leetcode: Delete Node in a Linked List
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 题目中已经说明了,node不是尾结点
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

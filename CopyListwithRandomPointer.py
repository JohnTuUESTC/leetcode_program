#coding:utf-8
'''
leetcode: Copy List with Random Pointer
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        self.step_1(head)
        self.step_2(head)
        return self.step_3(head)

    # 在原链表每一个结点的后面,插入一个与之一样的结点
    def step_1(self, head):
        node = head

        while node:
            temp_node = RandomListNode(node.label)
            temp_node.next = node.next
            node.next = temp_node

            node = temp_node.next

    # 将被复制结点的random指针连接上
    def step_2(self, head):
        node = head

        while node:
            temp_node = node.next

            if node.random: # 避免node.random是None的情况
                temp_node.random = node.random.next

            node = temp_node.next

    # 将复制的链表从原链表中分离开
    def step_3(self, head):
        new_head = head.next # 被复制链表的头结点
        temp_node = new_head

        node = head
        node.next = temp_node.next
        node = node.next

        while node:
            temp_node.next = node.next
            temp_node = temp_node.next

            node.next = temp_node.next
            node = node.next

        return new_head

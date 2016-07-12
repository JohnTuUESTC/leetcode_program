#coding:utf-8
'''
leetcode: Linked List Cycle
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next: # 如果链表为空,或链表中只有一个结点
            return False

        p_slow = head
        p_fast = head.next

        while p_fast: # 如果链表是无环的,那么肯定是p_fast先到达末尾,故不需要对p_slow进行判断
            p_slow = p_slow.next # 一次走一步

            # p_fast一次走两步
            for i in range(2):
                if p_fast.next:
                    p_fast = p_fast.next
                else:
                    return False

                # 必须先走一步之后再判断,否则会有误判
                if p_fast == p_slow:
                    return True

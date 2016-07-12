#coding:utf-8
'''
leetcode: Remove Linked List Elements
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return None

        if not head.next and head.val == val:
            return None

        curr_node = head
        pre_node = None

        while curr_node:
            if curr_node.val == val:
                if not head.next: # 链表中可能有多个重复的值,造成删除后链表中只有一个结点,且与val值相同的情况
                    return None

                if not curr_node.next: # 表明要删除的结点是最后一个结点
                    pre_node.next = None
                    break
                else:
                    next_node = curr_node.next
                    curr_node.val = next_node.val
                    curr_node.next = next_node.next
                    continue

            pre_node = curr_node
            curr_node = curr_node.next

        return head

if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_1.next = node_2

    sol = Solution()
    head = sol.removeElements(node_1, 1)
    while head:
        print(head.val)
        head = head.next
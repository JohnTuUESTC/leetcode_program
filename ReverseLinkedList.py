#coding:utf-8
'''
leetcode: Reverse Linked List
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        # 非递归的解法
        new_head = None # 反转后的头结点
        pre = None
        curr = head

        while curr:
            next_node = curr.next

            if not curr.next: # 当遍历到了最后一个结点时
                new_head = curr

            curr.next = pre # 将结点反转

            pre = curr
            curr = next_node

        return new_head
        '''

        # 递归的解法
        if head:
            node = head
            head = self.reverse(node)

        return head

    def reverse(self, node):

        if not node.next: # 如果遍历到了最后一个结点
            return node

        new_head = self.reverse(node.next)

        # 反转结点
        node.next.next = node
        node.next = None # 时刻注意要将当前结点的next设置为None,因为随时都可能遇到头结点

        return new_head

if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2

    sol = Solution()
    head = sol.reverseList(node_1)

    while head:
        print(head.val),
        print(" "),
        head = head.next

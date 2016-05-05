#coding:gb2312
'''
leetcode: Reverse Linked List II
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        num = 1
        first = None # 存储m位置的指针n
        node_stack = [] # 存储需要翻转的结点的val值

        temp = head
        while temp:
            if num == m:
                first = temp

            if m <= num <= n:
                node_stack.append(temp.val)

            temp = temp.next
            num += 1

        node_stack.reverse()
        for i in range(len(node_stack)):
            first.val = node_stack[i]
            first = first.next

        return head

if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    #node_2.next = node_3
    #node_3.next = node_4
    #node_4.next = node_5
    sol = Solution()
    new_node = sol.reverseBetween(node_1, 1, 1)
    while new_node:
        print(new_node.val),
        new_node = new_node.next
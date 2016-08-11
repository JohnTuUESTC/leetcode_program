#coding:utf-8
'''
leetcode: Linked List Cycle II
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return None

        first = head
        last = head

        has_cycle = False

        # 找到有环链表中两个指针的相遇位置, 两者之间相差的步数刚好是一个环的长度
        while last:
            first = first.next

            if last.next:
                last = last.next.next
            else:
                break

            if first == last:
                has_cycle = True
                break
        # 假设链表起始位置到环的起始位置之间的长度是s, 环的起始位置到两者相遇之间的长度是m, 环的长度为r, 所用步数为k
        # 有 k = r = s + m,有s = r - m,将相遇位置的指针与指向链表开始位置的指针向中间移动,相遇位置就是链表的开始位置
        if has_cycle:
            tmp = head
            while tmp != first: # 有可能头结点就是环开始的位置
                tmp = tmp.next
                first = first.next
            return tmp
        else:
            return None

if __name__ == "__main__":
    node = ListNode(1)
    node.next = node
    sol = Solution()
    sol.detectCycle(node)

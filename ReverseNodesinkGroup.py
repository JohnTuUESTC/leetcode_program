#coding:gb2312
'''
leetcode: Reverse Nodes in k-Group
'''

import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or k == 0 or k == 1:
            return head

        first = head # ��¼k�����Ŀ�ʼ
        last = head # ��¼k������ĩβ�ĺ�һ��λ��
        temp_k = k - 1
        first_reverse = True # ��ʾ��һ�η�ת
        last_round = None #��¼��һ�ε�ĩβλ��,����������һ�η�ת��ͷλ��

        while True:
            # Ѱ��k�����Ŀ�ʼ�ͽ���λ��
            while temp_k > 0 and last != None:
                temp_k -= 1
                last = last.next

            # ���Ľ����С��k
            if temp_k > 0 or last == None:
                return head

            last = last.next

            # ��ʼ��ת
            temp_k = k - 2
            pre = first
            curr = first.next
            next_p = first.next.next

            if temp_k == 0:
                curr.next = pre

                # ����ǵ�һ�η�ת,��Ҫ�޸�ͷ���
                if first_reverse:
                    head = curr
                    first_reverse = False
                    last_round = first
                else:
                    # ����һ�η�ת��ͷλ�����ӵ���һ�η�ת��βλ��
                    last_round.next = curr
                    last_round = first

            else:
                while temp_k >= 0:
                    curr.next = pre

                    pre = curr
                    curr = next_p
                    if next_p != None:
                        next_p = next_p.next
                    temp_k -= 1

                if first_reverse:
                    head = pre
                    first_reverse = False
                    last_round = first
                else:
                    last_round.next = pre
                    last_round = first

            first.next = last
            first = last
            temp_k = k - 1

        return head

if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_7 = ListNode(7)
    node_8 = ListNode(8)
    node_9 = ListNode(9)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    node_8.next = node_9

    sol = Solution()
    head = sol.reverseKGroup(node_1, 3)
    while head != None:
        print(head.val),
        print("\t"),
        head = head.next
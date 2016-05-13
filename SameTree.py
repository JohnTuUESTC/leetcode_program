#coding:gb2312
'''
leetcode: Same Tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # ������������һ��Ϊ�ն���һ����Ϊ��,�򷵻�false
        if (p and not q) or (not p and q):
            return False

        # ���������㶼Ϊ��,�򷵻�true
        if not p and not q:
            return True

        # �����������ֵ����ͬ
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

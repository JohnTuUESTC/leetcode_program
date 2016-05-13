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

        # 两个结点如果有一个为空而另一个不为空,则返回false
        if (p and not q) or (not p and q):
            return False

        # 如果两个结点都为空,则返回true
        if not p and not q:
            return True

        # 如果两个结点的值不相同
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

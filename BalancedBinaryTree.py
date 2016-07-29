#coding:utf-8
'''
leetcode: Balanced Binary Tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        balanced, depth = self.IsBalance(root)

        return balanced

    def IsBalance(self, node):
        if not node:
            return [True, 0]

        left_balanced, left_depth = self.IsBalance(node.left)
        right_balanced, right_depth = self.IsBalance(node.right)

        if left_depth > right_depth:
            depth = left_depth + 1
        else:
            depth = right_depth + 1


        diff = left_depth - right_depth

        if left_balanced and right_balanced and -1 <= diff <= 1:
            return [True, depth]
        else:
            return [False, depth]

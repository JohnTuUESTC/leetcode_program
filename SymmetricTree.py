#coding:gb2312
'''
leetcode: Symmetric Tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        if not root.right and not root.left:
            return True

        if root.left and root.right:
            return self.IsSymmetric(root.left, root.right)

        return False

    def IsSymmetric(self, node_1, node_2):
        # 判断这两个结点的值是否相等
        if node_1.val != node_2.val:
            return False

        left = False
        if node_1.left and node_2.right:
            left = self.IsSymmetric(node_1.left, node_2.right)
        elif not node_1.left and not node_2.right:
            left = True

        right = False
        if node_1.right and node_2.left:
            right = self.IsSymmetric(node_1.right, node_2.left)
        elif not node_1.right and not node_2.left:
            right = True

        return left and right

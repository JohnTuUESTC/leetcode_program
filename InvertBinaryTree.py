#coding:utf-8
'''
leetcode: Invert Binary Tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        self.InvertTree(root)
        return root

    def InvertTree(self, node):
        # 如果遍历到了叶子结点
        if not node.left and not node.right:
            return

        # 交换当前结点的左右子树
        temp_node = node.left
        node.left = node.right
        node.right = temp_node

        if node.left:
            self.InvertTree(node.left)

        if node.right:
            self.InvertTree(node.right)

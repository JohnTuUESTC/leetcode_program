#coding:utf-8
'''
leetcode: Flatten Binary Tree to Linked List
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        node = root

        while node:
            if node.left:
                pre = node.left

                # 寻找左子树的左右结点
                while pre.right:
                    pre = pre.right

                pre.right = node.right
                node.right = node.left
                node.left = None

            node = node.right


if __name__ == "__main__":
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_1.left = node_2

    sol = Solution()
    sol.flatten(node_1)
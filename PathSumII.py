#coding:utf-8
'''
leetcode: Path Sum II
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        curr_path = [] # 表示当前的路径
        path = [] # 表示所有和为sum的路径
        curr_sum = 0 # 表示当前的和

        self.PathSum(root, curr_sum, sum, curr_path, path)

        return path

    def PathSum(self, node, curr_sum, sum, curr_path, path):
        # 判断是否到达叶结点
        if not node.left and not node.right:
            if curr_sum + node.val == sum:
                curr_path.append(node.val)
                path.append(curr_path)
                return
            else:
                return
        else:
            if node.left:
                self.PathSum(node.left, curr_sum + node.val, sum, curr_path + [node.val], path)

            if node.right:
                self.PathSum(node.right, curr_sum + node.val, sum, curr_path + [node.val], path)

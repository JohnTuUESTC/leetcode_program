#coding:gb2312
'''
leetcode: Validate Binary Search Tree
'''

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        TLE
        node_list = [] # 存储树先序遍历的结果
        self.inOrderWalker(root, node_list)

        node_list_1 = [x for x in node_list if node_list.count(x) == 1]

        if len(node_list) > len(node_list_1):
            return False

        if node_list_1 != node_list.sort():
            return False

        return True

    def inOrderWalker(self, root, node_list):
        if not root:
            return

        if root.left:
            self.inOrderWalker(root.left, node_list)

        node_list.append(root.val)

        if root.right:
            self.inOrderWalker(root.right, node_list)
    '''
        return self.isValid(root, -sys.maxint-1, sys.maxint)

    def isValid(self, root, min_value, max_value):
        if not root:
            return True

        if not min_value < root.val < max_value:
            return False

        return self.isValid(root.left, min_value, root.val) and self.isValid(root.right, root.val, max_value)

if __name__ == "__main__":
    node_1 = TreeNode(10)
    node_2 = TreeNode(5)
    node_3 = TreeNode(15)
    node_4 = TreeNode(6)
    node_5 = TreeNode(20)

    #node_1.left = node_2
    #node_1.right = node_3
    #node_3.left = node_4
    #node_3.right = node_5

    sol = Solution()
    print(sol.isValidBST(node_1))
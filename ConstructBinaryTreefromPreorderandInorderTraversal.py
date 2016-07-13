#coding:utf-8
'''
leetcode: Construct Binary Tree from Preorder and Inorder Traversal
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        '''
        #  Memory Limit Exceeded,但感觉accept的方法跟这个方法并没有区别,不知道什么原因
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        # 在中序遍历中寻找到根节点所在的位置
        root_index = inorder.index(preorder[0])

        # 分别构建左右子树
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])

        return root
        '''

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root_value = preorder.pop(0)
        root = TreeNode(root_value) # 将先序遍历的第一个结点作为根节点

        # 在中序遍历中寻找到根节点所在的位置
        root_index = inorder.index(root_value)

        # 分别构建左右子树
        root.left = self.buildTree(preorder, inorder[:root_index]) # 这里有可能root_index为-1
        root.right = self.buildTree(preorder, inorder[root_index + 1:])

        return root

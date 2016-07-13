#coding:utf-8
'''
leetcode: Construct Binary Tree from Inorder and Postorder Traversal
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 其实这与先序遍历是很相似的,先序遍历的第一个结点是根节点,而后续遍历则反过来,最后一个结点是根结点
        if len(inorder) == 0:
            return None

        root_value = postorder.pop()
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)

        # 一定要注意到子树的构建顺序,因为pop是一个不可逆的过程,所以一定是先建立右子树
        # 如果先建立左子树的话,index函数会出错
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root
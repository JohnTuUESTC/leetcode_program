#coding:gb2312
'''
leetcode: Binary Tree Inorder Traversal
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        stack = [] # 存储遍历结点的栈
        result = [] # 存粗结果

        node = root

        while len(stack) != 0 or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result

if __name__ == "__main__":
    node_1 = TreeNode(1)
    node_3 = TreeNode(3)
    node_2 = TreeNode(2)

    node_1.right = node_3
    node_3.left = node_2

    sol = Solution()
    print(sol.inorderTraversal(node_1))


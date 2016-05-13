#coding:gb2312
'''
leetcode: Binary Tree Level Order Traversal
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = [] # 存储返回的结果
        node_list = []
        node_list.append(root)

        while len(node_list) > 0:
            temp_result = [] # 存储这一层的结果
            temp_node_list = [] # 存储下一层的结点序列
            for i in range(len(node_list)):
                temp_result.append(node_list[i].val)

                if node_list[i].left:
                    temp_node_list.append(node_list[i].left)
                if node_list[i].right:
                    temp_node_list.append(node_list[i].right)

            result.append(temp_result)
            node_list = temp_node_list

        return result

if __name__ == "__main__":
    node_1 = TreeNode(3)
    node_2 = TreeNode(9)
    node_3 = TreeNode(20)
    node_4 = TreeNode(15)
    node_5 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3
    node_3.left = node_4
    node_3.right = node_5

    sol = Solution()
    print(sol.levelOrder(node_1))


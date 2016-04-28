#coding:gb2312
'''
leetcode: World Search
'''

import copy

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            if word[0] in board[i]:
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:  # 首先寻找到开始字符的位置
                        if self.FindWord(board, i, j, word, 1, [[i, j]]):  # 再去寻找之后字符
                            return True

        return False

    # 从board[m][n]位置开始,寻找单词word的第index字符
    # stack表示已经使用过的位置
    def FindWord(self, board, m, n, word, index, stack):

        # 如果查找单词的长度为0, 表示已经查找完毕
        if len(word) == index:
            return True

        stack_1 = []  # 存储有可能出现字符的位置

        # 向左搜寻
        if n > 0 and board[m][n - 1] == word[index] and [m, n - 1] not in stack:
            stack_1.append([m, n - 1])

        # 向右搜寻
        if n < len(board[0]) - 1 and board[m][n + 1] == word[index] and [m, n + 1] not in stack:
            stack_1.append([m, n + 1])

        # 向下搜寻
        if m < len(board) - 1 and board[m + 1][n] == word[index] and [m + 1, n] not in stack:
            stack_1.append([m + 1, n])

        # 向上搜寻
        if m > 0 and board[m - 1][n] == word[index] and [m - 1, n] not in stack:
            stack_1.append([m - 1, n])

        if len(stack_1) == 0:  # 表示没有可能的搜索位置
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.exist(["aa"], "aaa"))
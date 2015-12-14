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

        used_flag = [] #记录board中的字母是否已经被使用
        for i in range(len(board)):
            temp = []
            for j in range(len(board[i])):
                temp.append(0)
            used_flag.append(temp)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    temp_used_flag = copy.deepcopy(used_flag)
                    temp_used_flag[i][j] = 1

                    if self.FindWord(board, i - 1, j, word[1: len(word)], temp_used_flag):
                        return True

                    if self.FindWord(board, i, j - 1, word[1: len(word)], temp_used_flag):
                        return True

                    if self.FindWord(board, i + 1, j, word[1: len(word)], temp_used_flag):
                        return True

                    if self.FindWord(board, i, j + 1, word[1: len(word)], temp_used_flag):
                        return True

                    continue
                else:
                    continue

        return False

    #从board[m][n]位置开始,寻找单词word
    def FindWord(self, board, m, n, word, used_flag):
        #如果查找单词的长度为0, 表示已经查找完毕
        if len(word) == 0:
            return True

        #判断查找位置是否已经超出边界
        if m < 0 or m >= len(board):
            return False
        if n < 0 or n >= len(board[m]):
            return False

        if board[m][n] == word[0] and used_flag[m][n] == 0:
            temp_used_flag = copy.deepcopy(used_flag)
            temp_used_flag[m][n] = 1

            #查找相邻区域
            if self.FindWord(board, m - 1, n, word[1: len(word)], temp_used_flag):
                return True

            if self.FindWord(board, m, n - 1, word[1: len(word)], temp_used_flag):
                return True

            if self.FindWord(board, m + 1, n, word[1: len(word)], temp_used_flag):
                return True

            if self.FindWord(board, m, n + 1, word[1: len(word)], temp_used_flag):
                return True

            return False
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.exist(["CAA","AAA","BCD"], "AAB"))
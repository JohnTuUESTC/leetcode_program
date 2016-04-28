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
                    if board[i][j] == word[0]:  # ����Ѱ�ҵ���ʼ�ַ���λ��
                        if self.FindWord(board, i, j, word, 1, [[i, j]]):  # ��ȥѰ��֮���ַ�
                            return True

        return False

    # ��board[m][n]λ�ÿ�ʼ,Ѱ�ҵ���word�ĵ�index�ַ�
    # stack��ʾ�Ѿ�ʹ�ù���λ��
    def FindWord(self, board, m, n, word, index, stack):

        # ������ҵ��ʵĳ���Ϊ0, ��ʾ�Ѿ��������
        if len(word) == index:
            return True

        stack_1 = []  # �洢�п��ܳ����ַ���λ��

        # ������Ѱ
        if n > 0 and board[m][n - 1] == word[index] and [m, n - 1] not in stack:
            stack_1.append([m, n - 1])

        # ������Ѱ
        if n < len(board[0]) - 1 and board[m][n + 1] == word[index] and [m, n + 1] not in stack:
            stack_1.append([m, n + 1])

        # ������Ѱ
        if m < len(board) - 1 and board[m + 1][n] == word[index] and [m + 1, n] not in stack:
            stack_1.append([m + 1, n])

        # ������Ѱ
        if m > 0 and board[m - 1][n] == word[index] and [m - 1, n] not in stack:
            stack_1.append([m - 1, n])

        if len(stack_1) == 0:  # ��ʾû�п��ܵ�����λ��
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.exist(["aa"], "aaa"))
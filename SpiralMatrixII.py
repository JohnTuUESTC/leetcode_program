#coding:gb2312
'''
leetcode:Spiral Matrix II
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 0:
            return []

        matrix = [] #��¼����ֵ����

        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            matrix.append(temp)

        #������±�
        row = 0
        column = 0

        direction = 1 #��ʾ���ߵķ���
        curr_num = 1 #��ʾ��ǰ�������

        while (column + 1 < n and matrix[row][column + 1] == 0) or\
            (row + 1 < n and matrix[row + 1][column] == 0) or\
            (row - 1 >= 0 and matrix[row - 1][column] == 0) or\
                (column - 1 >= 0 and matrix[row][column - 1] == 0):

            matrix[row][column] = curr_num
            curr_num += 1

            #��Ҫ�ı�Ϊ��������
            if direction == 1 and\
                    (column + 1 == n or (column + 1 < n and matrix[row][column + 1] > 0)):
                direction = 2

            #��Ҫ�ı�Ϊ��������
            if direction == 2 and\
                    (row + 1 == n or (row + 1 < len(matrix) and matrix[row + 1][column] > 0)):
                direction = 3

            #��Ҫ�ı�Ϊ��������
            if direction == 3 and\
                    (column - 1 < 0 or (column - 1 >= 0 and matrix[row][column - 1] > 0)):
                direction = 4

            #��Ҫ�ı�Ϊ��������
            if direction == 4 and\
                    (row - 1 >= 0 and matrix[row - 1][column] > 0):
                direction = 1

            #��ʾ��������
            if direction == 1:
                column += 1
            #��ʾ��������
            elif direction == 2:
                row += 1
            #��ʾ��������
            elif direction == 3:
                column -= 1
            else:
                row -= 1

        matrix[row][column] = curr_num

        return matrix

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateMatrix(4))
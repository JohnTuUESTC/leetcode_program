#coding:gb2312
'''
leetcode: Spiral Matrix
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if len(matrix) == 0:
            return []

        visited_matrix = [] #��¼���ʹ��ľ���Ԫ��

        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(0)
            visited_matrix.append(temp)

        visited_list = [] #�洢����ֵ

        #������±�
        row = 0
        column = 0

        direction = 1 #��ʾ���ߵķ���

        while (column + 1 < len(matrix[0]) and visited_matrix[row][column + 1] == 0) or\
            (row + 1 < len(matrix) and visited_matrix[row + 1][column] == 0) or\
            (row - 1 >= 0 and visited_matrix[row - 1][column] == 0) or\
                (column - 1 >= 0 and visited_matrix[row][column - 1] == 0):

            visited_list.append(matrix[row][column])
            visited_matrix[row][column] = 1

            #��Ҫ�ı�Ϊ��������
            if direction == 1 and\
                    ((column + 1 == len(matrix[0]) and visited_matrix[row + 1][column] == 0) or (column + 1 < len(matrix[0]) and visited_matrix[row][column + 1] == 1)):
                direction = 2

            #��Ҫ�ı�Ϊ��������
            if direction == 2 and\
                    ((row + 1 == len(matrix) and visited_matrix[row][column - 1] == 0) or (row + 1 < len(matrix) and visited_matrix[row + 1][column] == 1)):
                direction = 3

            #��Ҫ�ı�Ϊ��������
            if direction == 3 and\
                    ((column - 1 < 0 and visited_matrix[row - 1][column] == 0) or (column - 1 >= 0 and visited_matrix[row][column - 1] == 1)):
                direction = 4

            #��Ҫ�ı�Ϊ��������
            if direction == 4 and\
                    (row - 1 >= 0 and visited_matrix[row - 1][column] == 1):
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

        visited_list.append(matrix[row][column])

        return visited_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]))

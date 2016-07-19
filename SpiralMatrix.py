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
        '''
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
        '''

        if len(matrix) == 0:
            return []

        index = 0 # ��ʾ��ǰȦ��ʼ��λ��
        row = len(matrix)
        column = len(matrix[0])
        ret = [] # �洢���������

        while row > 2 * index and column > 2 * index:
            self.SpiralOrder(matrix, row, column, index, ret)
            index += 1

        return ret

    def SpiralOrder(self, matrix, row, column, index, ret):
        end_x = column - 1 - index # �е���Զ��
        end_y = row - 1 -index # �е���Զ��

        # �����ҽ��б���
        for i in range(index, end_x + 1):
            ret.append(matrix[index][i])

        # ���ٶ�һ��ʱ,�Ż���ϵ��½��б���
        if end_y > index:
            for i in range(index + 1, end_y + 1):
                ret.append(matrix[i][end_x])

        # ����Ҫ��һ���Ҷ�һ��,�Ż���ҵ�����б���
        if end_y > index and end_x > index:
            for i in range(end_x - 1, index - 1, -1):
                ret.append(matrix[end_y][i])

        # ���ٶ�һ���Ҷ����вŻ�������ϱ���
        if end_x > index and end_y > index + 1:
            for i in range(end_y - 1, index, -1):
                ret.append(matrix[i][index])

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]))

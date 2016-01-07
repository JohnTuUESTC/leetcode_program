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

        matrix = [] #记录返回值矩阵

        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            matrix.append(temp)

        #矩阵的下标
        row = 0
        column = 0

        direction = 1 #表示行走的方向
        curr_num = 1 #表示当前填到的数字

        while (column + 1 < n and matrix[row][column + 1] == 0) or\
            (row + 1 < n and matrix[row + 1][column] == 0) or\
            (row - 1 >= 0 and matrix[row - 1][column] == 0) or\
                (column - 1 >= 0 and matrix[row][column - 1] == 0):

            matrix[row][column] = curr_num
            curr_num += 1

            #需要改变为向下行走
            if direction == 1 and\
                    (column + 1 == n or (column + 1 < n and matrix[row][column + 1] > 0)):
                direction = 2

            #需要改变为向左行走
            if direction == 2 and\
                    (row + 1 == n or (row + 1 < len(matrix) and matrix[row + 1][column] > 0)):
                direction = 3

            #需要改变为向上行走
            if direction == 3 and\
                    (column - 1 < 0 or (column - 1 >= 0 and matrix[row][column - 1] > 0)):
                direction = 4

            #需要改变为向右行走
            if direction == 4 and\
                    (row - 1 >= 0 and matrix[row - 1][column] > 0):
                direction = 1

            #表示向右行走
            if direction == 1:
                column += 1
            #表示向下行走
            elif direction == 2:
                row += 1
            #表示向左行走
            elif direction == 3:
                column -= 1
            else:
                row -= 1

        matrix[row][column] = curr_num

        return matrix

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateMatrix(4))
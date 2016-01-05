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

        visited_matrix = [] #记录访问过的矩阵元素

        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(0)
            visited_matrix.append(temp)

        visited_list = [] #存储返回值

        #矩阵的下标
        row = 0
        column = 0

        direction = 1 #表示行走的方向

        while (column + 1 < len(matrix[0]) and visited_matrix[row][column + 1] == 0) or\
            (row + 1 < len(matrix) and visited_matrix[row + 1][column] == 0) or\
            (row - 1 >= 0 and visited_matrix[row - 1][column] == 0) or\
                (column - 1 >= 0 and visited_matrix[row][column - 1] == 0):

            visited_list.append(matrix[row][column])
            visited_matrix[row][column] = 1

            #需要改变为向下行走
            if direction == 1 and\
                    ((column + 1 == len(matrix[0]) and visited_matrix[row + 1][column] == 0) or (column + 1 < len(matrix[0]) and visited_matrix[row][column + 1] == 1)):
                direction = 2

            #需要改变为向左行走
            if direction == 2 and\
                    ((row + 1 == len(matrix) and visited_matrix[row][column - 1] == 0) or (row + 1 < len(matrix) and visited_matrix[row + 1][column] == 1)):
                direction = 3

            #需要改变为向上行走
            if direction == 3 and\
                    ((column - 1 < 0 and visited_matrix[row - 1][column] == 0) or (column - 1 >= 0 and visited_matrix[row][column - 1] == 1)):
                direction = 4

            #需要改变为向右行走
            if direction == 4 and\
                    (row - 1 >= 0 and visited_matrix[row - 1][column] == 1):
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

        visited_list.append(matrix[row][column])

        return visited_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]))

#coding:gb2312
'''
leetcode: Set Matrix Zeros
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        zero_row = [] #存储需要置0的行
        zero_column = [] #存储需要置0的列

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in zero_row:
                        zero_row.append(i)
                    if j not in zero_column:
                        zero_column.append(j)

        #将相应的行和列置0
        for row in zero_row:
            for column in range(len(matrix[0])):
                matrix[row][column] = 0

        for column in zero_column:
            for row in range(len(matrix)):
                matrix[row][column] = 0

        return matrix

if __name__ == "__main__":
    sol = Solution()
    print(sol.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))
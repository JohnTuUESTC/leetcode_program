#coding:gb2312
'''
leetcode:Rotate Image
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if len(matrix) == 0 or len(matrix) == 1:
            return

        first_row = 0
        last_row = len(matrix) - 1

        #将矩阵上下交换
        while first_row < last_row:
            for j in range(len(matrix)):
                temp = matrix[last_row][j]
                matrix[last_row][j] = matrix[first_row][j]
                matrix[first_row][j] = temp
            first_row += 1
            last_row -= 1

        #将矩阵沿主对角线进行交换
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i < j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        return matrix

if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
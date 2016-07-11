#coding:gb2312
'''
leetcode: Search a 2D Matrix
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        row = len(matrix) - 1
        column = len(matrix[0]) - 1

        target_row = -1 #表示target可能所在的行

        for i in range(len(matrix)):
            #target可能出现在某一行中
            if matrix[i][0] <= target <= matrix[i][column]:
                target_row = i
                break

        if target_row == -1:
            return False
        else:
            for j in range(column + 1):
                if matrix[target_row][j] == target:
                    return True
                elif matrix[target_row][j] > target:
                    return False
        '''
        row = len(matrix)
        column = len(matrix[0])

        if row > 0 and column > 0:
            # 从矩阵的右上角开始寻找
            curr_row = 0
            curr_column = column - 1
            while curr_row < row and curr_column >= 0:
                if target == matrix[curr_row][curr_column]:
                    return True
                elif target < matrix[curr_row][curr_column]: # 当前元素是这一列的最小值,如果小于的话,则说明不在这一行
                    curr_column -= 1
                else: # 当前元素是这一行的最大值,如果大于的话，说明不在这一行
                    curr_row += 1
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 11))
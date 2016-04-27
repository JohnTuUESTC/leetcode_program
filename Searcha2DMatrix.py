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

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 12))
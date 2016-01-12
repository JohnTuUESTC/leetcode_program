#coding:gb2312
'''
leetcode: Minimum Path Sum
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        path = [] #记录路径值的矩阵

        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(0)
            path.append(temp)

        path[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i - 1 < 0:
                    path[i][j] = path[i][j - 1] + grid[i][j]
                elif j - 1 < 0:
                    path[i][j] = path[i - 1][j] + grid[i][j]
                else:
                    if path[i][j - 1] < path[i - 1][j]:
                        path[i][j] = path[i][j - 1] + grid[i][j]
                    else:
                        path[i][j] = path[i - 1][j] + grid[i][j]

        return path[len(grid) - 1][len(grid[0]) - 1]

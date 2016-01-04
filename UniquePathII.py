#coding:gb2312
'''
leetcode: Unique Path II
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        path_num = [] #记录左上角结点到每一个结点的不同路径的条数

        for i in range(len(obstacleGrid)):
            temp = []

            for j in range(len(obstacleGrid[0])):
                temp.append(0)

            path_num.append(temp)

        if obstacleGrid[0][0] == 0:
            path_num[0][0] = 1

        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1: #如果该位置是个障碍位置
                    continue

                #将来自不同方向的路径数汇总
                if i - 1 >= 0:
                    path_num[i][j] += path_num[i - 1][j]

                if j - 1 >= 0:
                    path_num[i][j] += path_num[i][j - 1]

        return path_num[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[1]]))


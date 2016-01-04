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

        path_num = [] #��¼���Ͻǽ�㵽ÿһ�����Ĳ�ͬ·��������

        for i in range(len(obstacleGrid)):
            temp = []

            for j in range(len(obstacleGrid[0])):
                temp.append(0)

            path_num.append(temp)

        if obstacleGrid[0][0] == 0:
            path_num[0][0] = 1

        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1: #�����λ���Ǹ��ϰ�λ��
                    continue

                #�����Բ�ͬ�����·��������
                if i - 1 >= 0:
                    path_num[i][j] += path_num[i - 1][j]

                if j - 1 >= 0:
                    path_num[i][j] += path_num[i][j - 1]

        return path_num[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[1]]))


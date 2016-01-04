#coding:gb2312
'''
leetcode: Triangle
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]

        minimum_sum = [] #记录到每一个位置的最小和

        for i in range(len(triangle)):
            temp = []
            for j in range(len(triangle[i])):
                temp.append(0)
            minimum_sum.append(temp)

        minimum_sum[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    minimum_sum[i][j] = minimum_sum[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    minimum_sum[i][j] = minimum_sum[i - 1][j - 1] + triangle[i][j]
                else:
                    if minimum_sum[i - 1][j - 1] < minimum_sum[i - 1][j]:
                        minimum_sum[i][j] = minimum_sum[i - 1][j - 1] + triangle[i][j]
                    else:
                        minimum_sum[i][j] = minimum_sum[i - 1][j] + triangle[i][j]

        return min(minimum_sum[len(minimum_sum) - 1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
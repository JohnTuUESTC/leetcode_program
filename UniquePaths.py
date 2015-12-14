#coding:gb2312
'''
leetcode: Unique Paths
'''

#该问题主要计算c(m+n, m)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0 or n == 0:
            return 0

        if m == 1 or n == 1:
            return 1

        m -= 1
        n -= 1

        if m < n:
            temp = 1
            for i in range(n + 1, m + n + 1):
                temp *= i
            return temp / self.cal_factorial(m)
        else:
            temp = 1
            for i in range(m + 1, m + n + 1):
                temp *= i
            return temp / self.cal_factorial(n)

    def cal_factorial(self, m):
        if m == 1:
            return 1
        else:
            return m * self.cal_factorial(m - 1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(23, 12))

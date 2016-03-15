#coding:gb2312
'''
leetcode: Climbing Stairs
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 给出边界条件
        if n == 1:
            return 1

        if n == 2:
            return 2

        first = 1
        last = 2

        result = 0

        for i in range(3, n + 1):
            result = first + last
            first = last
            last = result

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(35))
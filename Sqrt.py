#coding:gb2312
'''
leetcode: Sqrt(x)
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        if x == 0:
            return 0
        elif x < 4:
            return 1

        result = 2 * self.mySqrt(x / 4)

        if (result + 1) ** 2 <= x:
            return result + 1

        return result
        '''
        # 牛顿法
        y = 1
        n = x
        while n > y:
            n = y + (n - y) / 2
            y = x / n
        return n

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(1015572837))
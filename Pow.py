#coding:gb2312
'''
leetcode: pow(x,n)
'''

import math

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0

        if n == 0:
            return 1

        negetive_flag = False
        if x < 0 and n % 2 == 1:
            negetive_flag = True

        result = 1
        temp_x = x

        if n < 0:
            n = abs(n)
            temp_x = 1 / float(x)

        #以平方阶速度增长
        temp_n = 1

        while temp_n < n:
            temp_x *= temp_x
            temp_n <<= 1

        if temp_n > n:
            temp_n >>= 1
            temp_x = math.sqrt(temp_x)

        while n > 0:
            if n >= temp_n:
                n -= temp_n
                result *= temp_x

            temp_n >>= 1
            temp_x = math.sqrt(temp_x)

        if negetive_flag:
            return -result
        else:
            return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(-13.62608,3))
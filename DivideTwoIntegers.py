#coding:gb2312
'''
leetcode: Divide Two Integers
'''

import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # 如果有除0错误
        if divisor == 0:
            return 2147483647

        if dividend == 0:
            return 0

        negetive_flag = False

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negetive_flag = True

        result = 0  # 记录除法的结果

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        dividend = abs(dividend)
        divisor = abs(divisor)
        bit = 1

        # 不断将除数累加
        while divisor < dividend:
            divisor <<= 1
            bit <<= 1

        if divisor > dividend:
            divisor >>= 1
            bit >>= 1

        while bit >= 1:
            if dividend >= divisor:
                dividend -= divisor
                result += bit

            bit >>= 1
            divisor >>= 1

        if negetive_flag:
            return -result

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(-2147483648, -2147483648))



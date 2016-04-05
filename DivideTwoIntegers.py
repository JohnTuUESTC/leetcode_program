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

        # ����г�0����
        if divisor == 0:
            return 2147483647

        if dividend == 0:
            return 0

        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            else:
                return -dividend

        negetive_flag = False

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negetive_flag = True

        result = 0  # ��¼�����Ľ��

        dividend = abs(dividend)
        divisor = abs(divisor)
        bit = 1

        # ���Ͻ������ۼ�
        while (divisor << 1) <= dividend:
            divisor <<= 1
            bit <<= 1

        while bit >= 1:
            if dividend > divisor:
                dividend -= divisor
                result += bit
            elif dividend == divisor:
                result += bit
                if negetive_flag:
                    return -result
                else:
                    return result

            bit >>= 1
            divisor >>= 1

        if negetive_flag:
            return -result

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(-2147483648, -2147483648))



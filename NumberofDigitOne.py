#coding:utf-8
'''
leetcode: Number of Digit One
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        num_str = str(n)

        return self.CountDigitOne(num_str)

    def CountDigitOne(self, num_str):
        if len(num_str) == 1:
            if num_str[0] == '0':
                return 0
            else:
                return 1

        # 计算最高位上的1出现的次数
        first_part = 0
        if num_str[0] >= '2':
            first_part = pow(10, len(num_str) - 1)
        elif num_str[0] == '1': # 这里必须要写明是1,因为可能出现0的情况
            first_part = int(num_str[1:]) + 1

        # 除最高位以外其他位上1出现的次数
        last_part = int(num_str[0]) * (len(num_str) - 1) * pow(10, len(num_str) - 2)

        other_part = self.CountDigitOne(num_str[1:])

        return first_part + last_part + other_part

if __name__ == "__main__":
    sol = Solution()
    print(sol.countDigitOne(100))

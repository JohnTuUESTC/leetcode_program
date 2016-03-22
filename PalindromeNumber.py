#coding:gb2312
'''
leetcode: Palindrome Number
'''

import copy

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x == 0:
            return True

        if x > 0:
            x_str = str(x)
        else:
            return False

        temp_x_str = x_str[::-1] # 将字符串进行翻转
        if x_str == temp_x_str:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1221))

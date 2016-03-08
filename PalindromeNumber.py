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
            temp_x = copy.deepcopy(x)
        else:
            return False

        x_reverse = 0

        #通过倒序获取原数的每一位来重构出原数
        while temp_x > 0:
            x_reverse *= 10
            x_reverse += temp_x % 10
            temp_x /= 10

        if x_reverse == x:
            return True

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(12321))

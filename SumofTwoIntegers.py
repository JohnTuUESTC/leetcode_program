#coding:utf-8
'''
leetcode: Sum of Two Integers
'''

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        sums = a

        while b:
            sums = a ^ b
            b = (a & b) << 1
            a = sums

        return sums

if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(-14, 16))
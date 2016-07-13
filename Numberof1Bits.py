#coding:utf-8
'''
leetcode: Number of 1 Bits
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1 # 将n与n - 1进行按位与,可以去掉n中最右边的1
            count += 1

        return count

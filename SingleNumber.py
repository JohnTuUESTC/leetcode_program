#coding: utf-8
'''
leetcode: Single Number
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        ret = 0
        for i in range(len(nums)):
            ret ^= nums[i]

        return ret
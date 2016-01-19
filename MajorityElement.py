# coding:gb2312
'''
leetcode: Majority Element
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        element_num = {} # �洢������ÿһ����ͬԪ�س��ֵĴ���

        for i in range(len(nums)):
            if nums[i] in element_num:
                element_num[nums[i]] += 1
            else:
                element_num[nums[i]] = 1

        for i in element_num:
            if element_num[i] > len(nums) / 2:
                return i
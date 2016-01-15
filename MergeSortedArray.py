#coding:gb2312
'''
leetcode: Merge Sorted Array
'''

import copy

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        temp_nums = copy.deepcopy(nums1)

        index_1 = 0 #记录temp_nums的位置
        index_2 = 0 #记录nums2的位置
        index_3 = 0 #记录nums1的位置

        while index_1 < m and index_2 < n:
            if temp_nums[index_1] < nums2[index_2]:
                nums1[index_3] = temp_nums[index_1]
                index_1 += 1
            else:
                nums1[index_3] = nums2[index_2]
                index_2 += 1
            index_3 += 1

        if index_1 < m:
            nums1[index_3:m + n] = temp_nums[index_1:m]
        if index_2 < n:
            nums1[index_3:m + n] = nums2[index_2:n]

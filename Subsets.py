#coding:gb2312
'''
leetcode: Subsets
'''

import copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []

        nums.sort() #���Ƚ������ź���

        subset = [[]] #�洢���������еļ���

        for i in range(len(nums)):
            temp_subset = copy.deepcopy(subset)
            for j in range(len(subset)):
                temp_subset[j].append(nums[i])
            subset = subset + temp_subset
        return subset

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1,2,2]))

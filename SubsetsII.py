#coding:gb2312
'''
leetcode: Subsets II
'''

import copy

class Solution(object):
    def subsetsWithDup(self, nums):
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

            #���ظ���Ԫ���޳�
            for j in temp_subset:
                if j not in subset:
                    subset.append(j)

        return subset

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))
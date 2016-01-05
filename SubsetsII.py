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

        nums.sort() #首先将序列排好序

        subset = [[]] #存储所有子序列的集合

        for i in range(len(nums)):
            temp_subset = copy.deepcopy(subset)
            for j in range(len(subset)):
                temp_subset[j].append(nums[i])

            #将重复的元素剔除
            for j in temp_subset:
                if j not in subset:
                    subset.append(j)

        return subset

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))
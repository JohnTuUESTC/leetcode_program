#coding:gb2312
'''
leetcode: Permutations
'''

import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        curr = [] #存储当前的结果
        permutations = [] #存储所有可能的排列

        self.find_permutations(nums, curr, permutations)

        return permutations

    def find_permutations(self, nums, curr, permutations):
        if len(nums) == 0 and curr not in permutations:
            permutations.append(curr)
            return

        for i in range(len(nums)):
            temp_nums = copy.deepcopy(nums)
            temp_curr = copy.deepcopy(curr)
            temp_curr.append(nums[i])
            temp_nums = temp_nums[0:i] + temp_nums[i + 1:len(temp_nums)]
            self.find_permutations(temp_nums, temp_curr, permutations)

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,1,2]))
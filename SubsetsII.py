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
        last_num = None
        dulplicated = 0 #记录重复元素的个数

        for i in range(len(nums)):
            if last_num == nums[i]:
                dulplicated += 1
            else:
                last_num = nums[i]
                dulplicated = 0

            temp_subset = copy.deepcopy(subset)

            # 如果当前没有重复元素,则可以在原来集合的每一项中添加当前元素
            if dulplicated == 0:
                for j in range(len(temp_subset)):
                    temp_subset[j].append(nums[i])

                subset += temp_subset
            else:
                # 如果有重复元素,那么只在出现重复元素个数等于当前重复元素个数的项中添加
                # 否则就会出现重复的项
                for j in range(len(temp_subset)):
                    if nums[i] in temp_subset[j] and temp_subset[j].count(nums[i]) == dulplicated:
                        subset += [temp_subset[j] + [nums[i]]]

        return subset

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2,3,3]))
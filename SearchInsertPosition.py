#coding:gb2312
'''
leetcode: Search Insert Position
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        #如果目标元素比第一个值都小
        if nums[0] > target:
            return 0

        #如果目标元素比第一个值都大
        if nums[len(nums) - 1] < target:
            return len(nums)

        for i in range(len(nums)):
            #如果恰好找到了目标元素
            if nums[i] == target:
                return i
            #如果恰好出现在某两个元素中间
            elif i < len(nums) - 1 and nums[i] < target and nums[i + 1] > target:
                return i + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 0))
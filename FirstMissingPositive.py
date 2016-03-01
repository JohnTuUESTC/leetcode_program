#coding:gb2312
'''
leetcode: First Missing Positive
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 1

        # 将正整数i放在i-1的位置上
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] != i + 1 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1]))

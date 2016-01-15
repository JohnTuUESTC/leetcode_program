# coding:gb2312
'''
leetcode: Maximum Subarray
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        curr_sum = 0 # 记录当前的和值
        max_sum = -1000 # 记录最大的和值

        for i in range(len(nums)):
            # 判断是否要将当前序列进行下去
            # 还是重新开始一个序列
            if curr_sum >= 0:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

        return  max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-1, -2]))
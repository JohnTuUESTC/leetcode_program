# coding:gb2312
'''
leetcode: Maximum Product Subarray
'''

import copy

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Time Limit Exceeded
        if len(nums) == 1:
            return nums[0]

        product = copy.deepcopy(nums) #记录每个位置处子序列的最大乘积

        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if product[j] < product[j] * nums[j - i]:
                    product[j] = product[j] * nums[j - i]

        return max(product)
        '''
        curr_min = nums[0] # 记录当前的最小值
        curr_max = nums[0] # 记录当前的最大值
        max_product = nums[0] # 当前的最大乘积

        for i in range(1, len(nums)):
            temp_1 = curr_min * nums[i]
            temp_2 = curr_max * nums[i]

            # 注意到,如果之前元素是0,那么序列的最大值或最小值需要重新开始计算
            if temp_2 > temp_1:
                if temp_2 > nums[i]:
                    curr_max = temp_2
                else:
                    curr_max = nums[i]
                if temp_1 < nums[i]:
                    curr_min = temp_1
                else:
                    curr_min = nums[i]
            else: # 如果是乘以负数的情况
                if temp_2 < nums[i]:
                    curr_min = temp_2
                else:
                    curr_min = nums[i]
                if temp_1 > nums[i]:
                    curr_max = temp_1
                else:
                    curr_max = nums[i]

            if max_product < curr_max:
                max_product = curr_max

        return  max_product
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([-5, 0,1, -2,3,4]))
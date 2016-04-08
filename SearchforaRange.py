#coding:gb2312
'''
leetcode: Search for a Range
'''

import math

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        '''
        high = len(nums) - 1
        low = 0
        target_index = -1

        #利用二分法来寻找合适的下标
        while low <= high:
            middle = (high + low) / 2
            if nums[middle] == target:
                target_index = middle
                break
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1

        if target_index == -1:
            return [-1,-1]

        first_index = target_index #target下标区间的下界
        last_index = target_index #target下标区间的上界

        #向前和向后寻找target的范围
        while first_index > 0:
            if nums[first_index] != nums[first_index - 1]:
                break
            first_index -= 1

        while last_index < len(nums) - 1:
            if nums[last_index + 1] != nums[last_index]:
                break
            last_index += 1

        return [first_index, last_index]
        '''
        range_first = self.lower_bound(nums, target) # 求出target的第一个元素
        range_last = self.lower_bound(nums, target + 1) # 求出target + 1的第一个元素

        # 如果target不在nums中的话,直接返回[-1,-1]
        if range_first < len(nums) and nums[range_first] == target:
            return [range_first, range_last - 1]
        else:
            return [-1, -1]

    # 计算出在list中一个元素第一次出现的位置
    def lower_bound(self, nums, target):
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) / 2

            if nums[mid] >= target:
                last = mid - 1
            else:
                first = mid + 1

        return first

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([2,2], 2))





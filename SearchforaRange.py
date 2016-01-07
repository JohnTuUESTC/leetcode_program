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

        if target not in nums:
            return [-1, -1]

        high = len(nums) - 1
        low = 0
        target_index = 0

        #利用二分法来寻找合适的下标
        while low <= high:
            middle = int(math.ceil((high + low) // 2))
            if nums[middle] == target:
                target_index = middle
                break
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1

        first_index = target_index #target下标区间的下界
        last_index = target_index #target下标区间的上界

        #向前和向后寻找target的范围
        if nums[0] == target:
            first_index = 0
        else:
            while first_index > 0:
                if nums[first_index - 1] != target:
                    break
                first_index -= 1

        if nums[len(nums) - 1] == target:
            last_index = len(nums) - 1
        else:
            while last_index < len(nums) - 1:
                if nums[last_index + 1] != target:
                    break
                last_index += 1

        return [first_index, last_index]

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([1,2,3], 3))





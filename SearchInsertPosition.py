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
        '''
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid - 1
            else:
                first = mid + 1

        return first
        '''
        index = 0
        while index < len(nums) and nums[index] < target:
            index += 1
        return index

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 3))
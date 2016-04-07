# coding:gb2312
'''
leetcode: Search in Rotated Sorted Array
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) / 2

            if nums[mid] == target:
                return mid

            # 位于单调递增区间的情况
            if nums[first] <= target < nums[mid]:
                last = mid - 1
            elif nums[mid] < target <= nums[last]:
                first = mid + 1

            # 位于有断点的区间内,判断在左还是右
            elif nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid - 1
        return -1

        #return self.BinarySearch(nums, 0, len(nums) - 1, target)


    def BinarySearch(self, nums, first, last, target):
        if first > last:
            return -1

        mid = (first + last) / 2
        '''
        if nums[first] == target:
            return first
        if nums[mid] == target:
            return mid
        if nums[last] == target:
            return last

        # 是一个单调增长的区间
        if nums[first] < nums[last]:
            if target < nums[first] or target > nums[last]:
                return -1
            if nums[mid] < target:
                return self.BinarySearch(nums, mid + 1, last, target)
            else:
                return self.BinarySearch(nums, first, mid - 1, target)
        # mid位于上半单调区间
        elif nums[last] < nums[first] < nums[mid]:
            if nums[first] < target < nums[mid]:
                return self.BinarySearch(nums, first, mid - 1, target)
            else:
                return self.BinarySearch(nums, mid + 1, last, target)
        else:
            if nums[mid] < target < nums[last]:
                return self.BinarySearch(nums, mid + 1, last, target)
            else:
                return self.BinarySearch(nums, first, mid - 1, target)
        '''

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([1,3], 3))
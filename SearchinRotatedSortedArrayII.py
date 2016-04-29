#coding:gb2312
'''
leetcode: Search in Rotated Sorted Array II
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) / 2

            if nums[mid] == target:
                return True

            # 将重复的元素去除掉
            while first < mid and nums[first] == nums[mid]:
                first += 1

            # 表示左半边元素是有序的
            if nums[first] <= nums[mid]:
                if nums[first] <= target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[mid] < target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([1,3,1,1,1], 3))

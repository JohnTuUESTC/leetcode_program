#coding:gb2312
'''
leetcode: Missing Number
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 1

        self.quick_sort(nums, 0, len(nums) - 1)

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)

    def quick_sort(self, nums, m, n):
        if m >= n:
            return

        first = m
        last = m - 1

        while first < n:
            if nums[first] < nums[n]:
                last += 1
                temp = nums[first]
                nums[first] = nums[last]
                nums[last] = temp
            first += 1

        temp = nums[last + 1]
        nums[last + 1] = nums[n]
        nums[n] = temp

        self.quick_sort(nums, last + 2, n)
        self.quick_sort(nums, m, last)

if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([0,1,3]))



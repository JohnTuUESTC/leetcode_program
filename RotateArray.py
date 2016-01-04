#coding:gb2312
'''
leetcode: Rotate Array
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if k > len(nums):
            k %= len(nums)

        nums = self.list_rotate(nums, len(nums) - k, len(nums) - 1)
        nums = self.list_rotate(nums, 0, len(nums) - k - 1)
        nums = self.list_rotate(nums, 0, len(nums) - 1)
        print(nums)

    def list_rotate(self, num_list, first, last):
        while first < last:
            temp = num_list[last]
            num_list[last] = num_list[first]
            num_list[first] = temp
            first += 1
            last -= 1
        return num_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([1,2,3,4,5,6], 11))
#coding:gb2312
'''
leetcode: Next Permutation
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        index_1 = -1
        index_2 = -1

        #找到排列中最右一个升序的首位位置
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index_1 = i
                break

        #表示已经是全排列的最后一个,则将其反转
        if index_1 == -1:
            self.reverse_list(nums, 0, len(nums) - 1)
            return nums

        #寻找index_1右边第一个比index_1大的位置
        for i in range(len(nums) - 1, index_1, -1):
            if nums[i] > nums[index_1]:
                index_2 = i
                break

        #交换index_1和index_2对应的值
        temp = nums[index_1]
        nums[index_1] = nums[index_2]
        nums[index_2] = temp

        #将index_1之后的部分反转
        self.reverse_list(nums, index_1 + 1, len(nums) - 1)

        return nums

    def reverse_list(self, nums, m, n):
        while m < n:
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp
            m += 1
            n -= 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.nextPermutation([1,3,2]))
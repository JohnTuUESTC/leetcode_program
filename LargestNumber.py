#coding:utf-8
'''
leetcode: Largest Number
'''

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if len(nums) == 0:
            return ''

        self.Sorted(nums, 0, len(nums) - 1)

        ret = ''
        for i in range(len(nums)):
            ret += str(nums[i])

        # 去除头部可能多余的0
        while len(ret) > 1:
            if ret[0] > '0':
                return ret
            else:
                ret = ret[1:]

        return ret

    def Sorted(self, nums, first, last):
        if first >= last:
            return

        index_1 = first - 1
        index_2 = first

        while index_2 < last:
            if self.SortNumber(nums[index_2], nums[last]):
                index_1 += 1
                temp = nums[index_2]
                nums[index_2] = nums[index_1]
                nums[index_1] = temp

            index_2 += 1

        temp = nums[last]
        nums[last] = nums[index_1 + 1]
        nums[index_1 + 1] = temp

        self.Sorted(nums, first, index_1)
        self.Sorted(nums, index_1 + 2, last)

    # 根据两个数组成的数的大小判断它们之间的相关次序
    def SortNumber(self, num_1, num_2):
        num1 = str(num_1) + str(num_2)
        num2 = str(num_2) + str(num_1)

        if cmp(num1, num2) == -1 or cmp(num1, num2) == 0:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([10]))

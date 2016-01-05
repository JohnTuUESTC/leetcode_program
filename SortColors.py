#coding:gb2312
'''
leetcode: Sort Colors
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        begin = 0 #记录序列的开始位置
        end = len(nums) - 1 #记录序列的结束位置
        curr = 0 #表示当前所在位置

        while curr <= end:
            #如果当前数字为0,则与开始数字交换
            if nums[curr] == 0:
                temp = nums[curr]
                nums[curr] = nums[begin]
                nums[begin] = temp

                begin += 1
                curr += 1
            #如果当前数字为1, 则不做任何处理
            elif nums[curr] == 1:
                curr += 1
            #如果当前数字为2,则与结尾数字交换
            else:
                nums[curr] = nums[end]
                nums[end] = 2
                end -= 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors([0,1,2,1,1,2,0,2,1,0]))
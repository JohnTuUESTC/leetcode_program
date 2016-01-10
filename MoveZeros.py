#coding:gb2312
'''
leetcode: Move Zeros
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        first = 0
        end = -1 #记录第一个0元素的位置

        while first < len(nums):
            #将end指向第一个0元素所在的位置
            if nums[first] == 0 and end < 0:
                end = first
            #将0元素移动到后面
            if nums[first] != 0 and first != end and end >= 0:
                nums[end] = nums[first]
                nums[first] = 0
                #如果first与end间隔1,那么加1刚好是移动到了交换过来的0元素的位置
                #如果中间还有0元素,那么前面就已经被跳过了,加1还是移动到了第一个0元素的位置
                end += 1
            first += 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([1]))
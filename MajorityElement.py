# coding:gb2312
'''
leetcode: Majority Element
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        element_num = {} # 存储序列中每一个不同元素出现的次数

        for i in range(len(nums)):
            if nums[i] in element_num:
                element_num[nums[i]] += 1
            else:
                element_num[nums[i]] = 1

        for i in element_num:
            if element_num[i] > len(nums) / 2:
                return i
        '''

        number = nums[0] # 存储出现次数超过一半的元素
        times = 1

        for i in range(1, len(nums)):
            if times == 0: # 出现次数超过一半的数字是使times变为1的最后一个数字
                number = nums[i]
                times = 1
            elif nums[i] == number: # 如果当前的数字与存储的数字相同
                times += 1
            else:
                times -= 1

        return number

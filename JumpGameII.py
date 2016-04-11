#coding:gb2312
'''
leetcode: Jump Game II
'''

import copy

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        if nums[0] == 0 or len(nums) == 0:
            return 0

        min_step = [0] #存储到达每一个位置的最小步数

        for i in range(1, len(nums)):
            min_step.append(len(nums))

        for i in range(1, len(nums)):
            for j in range(i):
                if j + nums[j] >= i and min_step[j] + 1 < min_step[i]:
                    min_step[i] = min_step[j] + 1
                    break

        return min_step[len(nums) - 1]
        '''

        if len(nums) <= 1:
            return 0

        cur_longest = nums[0] # 表示当前步能够移动的最远距离
        next_longest = nums[0] # 表示下一步能够移动的最远距离
        step = 1

        for i in range(1, len(nums)):
            if i > cur_longest: # 当前位置已经超出了当前步能够到达的最远位置,需要增加一步
                cur_longest = next_longest
                step += 1

            if i + nums[i] > next_longest:
                next_longest = i + nums[i]

            if cur_longest >= len(nums) - 1:
                return step


if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([1,1,1,1]))
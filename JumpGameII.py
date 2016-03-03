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
        超时
        path = [0] #存储到达末尾的路径
        min_step = [len(nums)] #存储最少使用的步数

        self.find_jump_path(nums, path, min_step)

        return min_step[0]

    def find_jump_path(self, nums, path, min_step):
        # 表示已经能够到达数组的末尾
        if nums[path[len(path) - 1]] + path[len(path) - 1] >= len(nums) - 1 and len(path) < min_step[0]:
            min_step[0] = len(path)
            return

        temp_path = copy.deepcopy(path)

        for i in range(1, nums[temp_path[len(temp_path) - 1]] + 1):
            if temp_path[len(temp_path) - 1] + i < len(nums):
                temp_path.append(temp_path[len(temp_path) - 1] + i)
                self.find_jump_path(nums, temp_path, min_step)
                temp_path.pop()
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([5,4,0,1,3,6,8,0,9,4,9,1,8,7,4,8]))
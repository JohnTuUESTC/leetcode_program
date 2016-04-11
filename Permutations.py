#coding:gb2312
'''
leetcode: Permutations
'''

import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        '''
        nums.sort()
        curr = nums #存储当前的结果
        permutations = [] #存储所有可能的排列
        permutations.append(curr)

        self.next_permutations(curr, permutations)

        return permutations

    def next_permutations(self, temp_curr, permutations):
        curr = copy.deepcopy(temp_curr)
        # 寻找最后一个升序的位置
        index = -1
        for i in range(len(curr) - 1, 0, -1):
            if curr[i - 1] < curr[i]:
                index = i - 1
                break

        if index != -1:
            # 寻找最后一个比curr[index]大的元素
            for i in range(len(curr) - 1, index, -1):
                if curr[i] > curr[index]:
                    temp = curr[index]
                    curr[index] = curr[i]
                    curr[i] = temp
                    break

            self.reverse_list(curr, index + 1, len(curr) - 1)
            permutations.append(curr)
            self.next_permutations(curr, permutations)

    def reverse_list(self, curr_list, first, last):
        while first < last:
            temp = curr_list[first]
            curr_list[first] = curr_list[last]
            curr_list[last] = temp
            first += 1
            last -= 1
    '''
        permutations = [[nums[0]]]  # 存储所有可能的排列

        for i in range(1, len(nums)):
            temp_permutations = []
            for j in range(len(permutations)):
                for index in range(len(permutations[0]) + 1):
                    temp_list = copy.deepcopy(permutations[j])
                    temp_list.insert(index, nums[i])
                    temp_permutations.append(temp_list)

            permutations = temp_permutations

        return permutations

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([0,-1,1]))
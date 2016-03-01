#coding:gb2312
'''
leetcode: Combination Sum
'''

import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        combination = [] # 存储所有可能的组合
        solution = [] #存储当前的组合

        candidates.sort()

        if target < candidates[0] or target == 0 or len(candidates) == 0:
            return []

        self.find_combin(candidates, target, solution, combination, 0)

        return combination

    #其中level表示当前从哪一个元素开始寻找
    def find_combin(self, candidates, target, solution, combination, level):
        #表示找到了一种组合
        if target == 0 and solution not in combination:
            combination.append(solution)
            return
        #表示不可能找到一种组合
        if target < 0:
            return

        temp_sol = copy.deepcopy(solution)

        for i in range(level, len(candidates)):
            temp_sol.append(candidates[i])
            target -= candidates[i]
            self.find_combin(candidates, target, temp_sol, combination, i)
            temp_sol = solution[0:len(temp_sol) - 1]
            target += candidates[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([8,7,4,3], 11))
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

        combination = [] # 存储结果
        solution = [] # 存储当前的组合

        candidates.sort()

        self.find_combin(candidates, target, solution, combination)

        return combination

    def find_combin(self, candidates, target, solution, combination):
        for i in range(len(candidates)):
            if target < candidates[i]:
                break
            elif target == candidates[i]:
                combination.append(solution + [candidates[i]])
                break
            else:
                self.find_combin(candidates[i:], target - candidates[i], solution + [candidates[i]], combination)


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([8,7,4,3], 11))
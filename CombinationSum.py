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

        combination = [] # �洢���п��ܵ����
        solution = [] #�洢��ǰ�����

        candidates.sort()

        if target < candidates[0] or target == 0 or len(candidates) == 0:
            return []

        self.find_combin(candidates, target, solution, combination, 0)

        return combination

    #����level��ʾ��ǰ����һ��Ԫ�ؿ�ʼѰ��
    def find_combin(self, candidates, target, solution, combination, level):
        #��ʾ�ҵ���һ�����
        if target == 0 and solution not in combination:
            combination.append(solution)
            return
        #��ʾ�������ҵ�һ�����
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
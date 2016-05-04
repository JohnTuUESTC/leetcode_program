#coding:gb2312
'''
leetcode: Subsets II
'''

import copy

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []

        nums.sort() #���Ƚ������ź���

        subset = [[]] #�洢���������еļ���
        last_num = None
        dulplicated = 0 #��¼�ظ�Ԫ�صĸ���

        for i in range(len(nums)):
            if last_num == nums[i]:
                dulplicated += 1
            else:
                last_num = nums[i]
                dulplicated = 0

            temp_subset = copy.deepcopy(subset)

            # �����ǰû���ظ�Ԫ��,�������ԭ�����ϵ�ÿһ������ӵ�ǰԪ��
            if dulplicated == 0:
                for j in range(len(temp_subset)):
                    temp_subset[j].append(nums[i])

                subset += temp_subset
            else:
                # ������ظ�Ԫ��,��ôֻ�ڳ����ظ�Ԫ�ظ������ڵ�ǰ�ظ�Ԫ�ظ������������
                # ����ͻ�����ظ�����
                for j in range(len(temp_subset)):
                    if nums[i] in temp_subset[j] and temp_subset[j].count(nums[i]) == dulplicated:
                        subset += [temp_subset[j] + [nums[i]]]

        return subset

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2,3,3]))
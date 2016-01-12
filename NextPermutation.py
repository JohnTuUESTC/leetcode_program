#coding:gb2312
'''
leetcode: Next Permutation
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        index_1 = -1
        index_2 = -1

        #�ҵ�����������һ���������λλ��
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index_1 = i
                break

        #��ʾ�Ѿ���ȫ���е����һ��,���䷴ת
        if index_1 == -1:
            self.reverse_list(nums, 0, len(nums) - 1)
            return nums

        #Ѱ��index_1�ұߵ�һ����index_1���λ��
        for i in range(len(nums) - 1, index_1, -1):
            if nums[i] > nums[index_1]:
                index_2 = i
                break

        #����index_1��index_2��Ӧ��ֵ
        temp = nums[index_1]
        nums[index_1] = nums[index_2]
        nums[index_2] = temp

        #��index_1֮��Ĳ��ַ�ת
        self.reverse_list(nums, index_1 + 1, len(nums) - 1)

        return nums

    def reverse_list(self, nums, m, n):
        while m < n:
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp
            m += 1
            n -= 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.nextPermutation([1,3,2]))
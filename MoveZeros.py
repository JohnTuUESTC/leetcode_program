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
        end = -1 #��¼��һ��0Ԫ�ص�λ��

        while first < len(nums):
            #��endָ���һ��0Ԫ�����ڵ�λ��
            if nums[first] == 0 and end < 0:
                end = first
            #��0Ԫ���ƶ�������
            if nums[first] != 0 and first != end and end >= 0:
                nums[end] = nums[first]
                nums[first] = 0
                #���first��end���1,��ô��1�պ����ƶ����˽���������0Ԫ�ص�λ��
                #����м仹��0Ԫ��,��ôǰ����Ѿ���������,��1�����ƶ����˵�һ��0Ԫ�ص�λ��
                end += 1
            first += 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([1]))
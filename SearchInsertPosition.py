#coding:gb2312
'''
leetcode: Search Insert Position
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        #���Ŀ��Ԫ�رȵ�һ��ֵ��С
        if nums[0] > target:
            return 0

        #���Ŀ��Ԫ�رȵ�һ��ֵ����
        if nums[len(nums) - 1] < target:
            return len(nums)

        for i in range(len(nums)):
            #���ǡ���ҵ���Ŀ��Ԫ��
            if nums[i] == target:
                return i
            #���ǡ�ó�����ĳ����Ԫ���м�
            elif i < len(nums) - 1 and nums[i] < target and nums[i + 1] > target:
                return i + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 0))
#coding:gb2312
'''
leetcode: Remove Duplicates from Sorted Array II
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        first = 0
        last = 1

        length = len(nums)
        dul_element = 0 # �ظ�Ԫ�صĸ���
        duplicated = False # ��ʾ��ǰ�Ƿ����ظ�Ԫ��

        while last < len(nums) - dul_element:
            if nums[first] == nums[last]:
                # ��ʾ��ǰ��Ԫ���ظ�
                if duplicated:
                    while last < len(nums) - dul_element and nums[last] == nums[first]:
                        dul_element += 1
                        for i in range(last, len(nums) - dul_element):
                            nums[i] = nums[i + 1]
                        duplicated = False
                else:
                    duplicated = True

            else:
                duplicated = False

            first = last
            last += 1

        return length - dul_element

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))



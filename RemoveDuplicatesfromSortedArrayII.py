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

        first = 0
        last = 1

        length = 0 # �����б�ĳ���
        duplicated = False # ��ʾ��ǰ�Ƿ����ظ�Ԫ��

        while last < len(nums) - length:
            if nums[first] == nums[last + length]: # ��ʾ��ǰ�ѳ������ظ���Ԫ��
                if duplicated:
                    length += 1
                else:
                    # ���ֻ������һ���ظ���Ԫ��
                    duplicated = True
                    nums[last] = nums[last + length]
                    first += 1
                    last += 1

            else:
                duplicated = False
                # �����ظ���Ԫ�ظ��Ƶ�ǰ��
                nums[last] = nums[last + length]
                first += 1
                last += 1

        return len(nums) - length

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))



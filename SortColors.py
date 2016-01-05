#coding:gb2312
'''
leetcode: Sort Colors
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        begin = 0 #��¼���еĿ�ʼλ��
        end = len(nums) - 1 #��¼���еĽ���λ��
        curr = 0 #��ʾ��ǰ����λ��

        while curr <= end:
            #�����ǰ����Ϊ0,���뿪ʼ���ֽ���
            if nums[curr] == 0:
                temp = nums[curr]
                nums[curr] = nums[begin]
                nums[begin] = temp

                begin += 1
                curr += 1
            #�����ǰ����Ϊ1, �����κδ���
            elif nums[curr] == 1:
                curr += 1
            #�����ǰ����Ϊ2,�����β���ֽ���
            else:
                nums[curr] = nums[end]
                nums[end] = 2
                end -= 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors([0,1,2,1,1,2,0,2,1,0]))
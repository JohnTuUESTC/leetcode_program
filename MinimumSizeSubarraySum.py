#coding:gb2312
'''
leetcode: Minimum Size Subarray Sum
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if s == 0 or s == 1:
            return 1

        first = 0
        last = 0
        curr_distance = s - nums[0] # �洢��ǰ��s֮��Ĳ�ֵ
        min_len = len(nums) + 1 # �洢��ǰ����̳���

        while first < len(nums) and last <= first:
            # �����ǰ�����еĺ���s���в��,��Ҫ��չ���ĳ���
            if curr_distance > 0:
                first += 1
                if first < len(nums):
                    curr_distance -= nums[first]
            else:
                if min_len > first - last + 1:
                    min_len = first - last + 1

                # ��ͼ���������еĳ���
                curr_distance += nums[last]
                last += 1

        if min_len == len(nums) + 1:
            return 0
        else:
            return  min_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(15, [1,2,3,4,5]))

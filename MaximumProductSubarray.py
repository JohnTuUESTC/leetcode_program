# coding:gb2312
'''
leetcode: Maximum Product Subarray
'''

import copy

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Time Limit Exceeded
        if len(nums) == 1:
            return nums[0]

        product = copy.deepcopy(nums) #��¼ÿ��λ�ô������е����˻�

        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if product[j] < product[j] * nums[j - i]:
                    product[j] = product[j] * nums[j - i]

        return max(product)
        '''
        curr_min = nums[0] # ��¼��ǰ����Сֵ
        curr_max = nums[0] # ��¼��ǰ�����ֵ
        max_product = nums[0] # ��ǰ�����˻�

        for i in range(1, len(nums)):
            temp_1 = curr_min * nums[i]
            temp_2 = curr_max * nums[i]

            # ע�⵽,���֮ǰԪ����0,��ô���е����ֵ����Сֵ��Ҫ���¿�ʼ����
            if temp_2 > temp_1:
                if temp_2 > nums[i]:
                    curr_max = temp_2
                else:
                    curr_max = nums[i]
                if temp_1 < nums[i]:
                    curr_min = temp_1
                else:
                    curr_min = nums[i]
            else: # ����ǳ��Ը��������
                if temp_2 < nums[i]:
                    curr_min = temp_2
                else:
                    curr_min = nums[i]
                if temp_1 > nums[i]:
                    curr_max = temp_1
                else:
                    curr_max = nums[i]

            if max_product < curr_max:
                max_product = curr_max

        return  max_product
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([-5, 0,1, -2,3,4]))
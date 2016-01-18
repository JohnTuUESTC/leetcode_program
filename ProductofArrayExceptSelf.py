# coding:gb2312
'''
leetcode: Product of Array Except Self
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [1]

        product = [] # 保存返回的结果
        right_product = [] # 记录一个数字右边的乘积
        left_product = [] # 记录一个数字左边的乘积

        for i in range(len(nums)):
            right_product.append(0)
            left_product.append(0)
            product.append(0)

        right_product[len(nums) - 1] = 1
        left_product[0] = 1

        for i in range(len(nums) - 1):
            left_product[i + 1] = left_product[i] * nums[i]

        for i in range(len(nums) - 1, 0, -1):
            right_product[i - 1] = right_product[i] * nums[i]

        for i in range(len(nums)):
            product[i] = left_product[i] * right_product[i]

        return product

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
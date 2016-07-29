#coding:utf-8
'''
leetcode: Single Number III
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ret = 0
        for i in range(len(nums)):
            ret ^= nums[i]

        bit = self.Last_One_Bit(ret)

        num_1 = 0
        num_2 = 0
        for i in range(len(nums)):
            # 对bit位是否为1对数组进行切分
            if self.Is_Bit_One(nums[i], bit):
                num_1 ^= nums[i]
            else:
                num_2 ^= nums[i]

        return [num_1, num_2]

    # 寻找最后一个为1的位
    def Last_One_Bit(self, num):
        bit = 0

        while num & 1 == 0:
            num >>= 1
            bit += 1

        return bit

    def Is_Bit_One(self, num, bit):
        num >>= bit

        if num & 1 == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([1, 2, 1, 3, 2, 5],))
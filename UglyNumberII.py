#coding:utf-8
'''
leetcode: Ugly Number II
'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return None

        index = 0
        ugly_number = [1] # 存储所有的丑数

        index_2 = index # 丑数中乘以2比最后一个数大的第一个数
        index_3 = index
        index_5 = index

        while index < n - 1:
            min_num = ugly_number[index_2] * 2
            if min_num > ugly_number[index_3] * 3:
                min_num = ugly_number[index_3] * 3

            if min_num > ugly_number[index_5] * 5:
                min_num = ugly_number[index_5] * 5

            ugly_number.append(min_num)

            while ugly_number[index_2] * 2 <= min_num:
                index_2 += 1

            while ugly_number[index_3] * 3 <= min_num:
                index_3 += 1

            while ugly_number[index_5] * 5 <= min_num:
                index_5 += 1

            index += 1

        return ugly_number[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.nthUglyNumber(3))

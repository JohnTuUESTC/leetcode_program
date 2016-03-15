#coding:gb2312
'''
leetcode: Sqrt(x)
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        TLE,可用二分搜索
        if x <= 0:
            return x

        first = 0
        last = 1

        while True:
            if 1 << first <= x <= 1 << last:
                break

            first += 1
            last += 1

        temp_1 = 1 << (first / 2)
        temp_2 = 1 << (last / 2)

        for i in range(temp_1, temp_2):
            result_1 = i ** 2
            result_2 = (i + 1) ** 2

            if result_1 == x:
                return i
            elif result_1 < x < result_2:
                return i
            elif result_2 == x:
                return i + 1
        '''


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(1015572837))
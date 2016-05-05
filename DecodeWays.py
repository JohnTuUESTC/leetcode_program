#coding:gb2312
'''
leetcode: Decode Ways
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        ways = [0] * (len(s) + 1)
        ways[0] = 1

        if s[0] != '0':
            ways[1] = 1

        for i in range(2, len(s) + 1):
            first_num = int(s[i - 1:i])

            # 表示前一个字符可以被单独解释
            if first_num > 0:
                ways[i] += ways[i - 1]

            second_num = int(s[i - 2:i])

            #表示前两个字符可以被单独解释
            if 10 <= second_num <= 26:
                ways[i] += ways[i - 2]

        return ways[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("27"))
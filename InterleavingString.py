#coding:gb2312
'''
leetcode: Interleaving String
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s3) != len(s1) + len(s2):
            return False
        '''
        # TLE
        s1 += " "
        s2 += " "
        # 当前遍历到的位置
        index_1 = 0
        index_2 = 0
        index_3 = 0
        # 保存可能需要回溯的位置
        index_1_stack = []
        index_2_stack = []
        index_3_stack = []

        while index_1 < len(s1) and index_2 < len(s2):
            # 如果字符串已经遍历完了
            if index_3 == len(s3):
                # 如果s1或是s2还没有到末尾,如果还有回溯的可能,需要回溯
                if index_1 == len(s1) - 1 and index_2 == len(s2) - 1:
                    return True
                elif len(index_1_stack) != 0:
                    index_1 = index_1_stack.pop()
                    index_2 = index_2_stack.pop() + 1
                    index_3 = index_3_stack.pop() + 1
                else:
                    return False

            if s1[index_1] == s3[index_3] and s2[index_2] != s3[index_3]:
                index_1 += 1
                index_3 += 1
                continue

            if s1[index_1] != s3[index_3] and s2[index_2] == s3[index_3]:
                index_2 += 1
                index_3 += 1
                continue

            if s1[index_1] == s3[index_3] and s2[index_2] == s3[index_3]:
                index_1_stack.append(index_1)
                index_1 += 1
                index_2_stack.append(index_2)
                index_3_stack.append(index_3)
                index_3 += 1
                continue

            # 如果与两字符串当前位置都不匹配的话，需要回溯
            if s1[index_1] != s3[index_3] and s2[index_2] != s3[index_3]:
                if len(index_1_stack) == 0:
                    return False
                else:
                    index_1 = index_1_stack.pop()
                    index_2 = index_2_stack.pop() + 1
                    index_3 = index_3_stack.pop() + 1
                continue
        '''
        # dp[i][j]表示s3[i + j - 1]是否是由s1[i - 1]和s2[j - 1]组成的
        dp = [[True for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]

        # 分别记录s1和s2在s3中连续出现的情况
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        # s1中前i个字符与s2中前j个字符的交叉组合是否在s3中出现
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
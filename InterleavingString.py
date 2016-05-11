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
        # ��ǰ��������λ��
        index_1 = 0
        index_2 = 0
        index_3 = 0
        # ���������Ҫ���ݵ�λ��
        index_1_stack = []
        index_2_stack = []
        index_3_stack = []

        while index_1 < len(s1) and index_2 < len(s2):
            # ����ַ����Ѿ���������
            if index_3 == len(s3):
                # ���s1����s2��û�е�ĩβ,������л��ݵĿ���,��Ҫ����
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

            # ��������ַ�����ǰλ�ö���ƥ��Ļ�����Ҫ����
            if s1[index_1] != s3[index_3] and s2[index_2] != s3[index_3]:
                if len(index_1_stack) == 0:
                    return False
                else:
                    index_1 = index_1_stack.pop()
                    index_2 = index_2_stack.pop() + 1
                    index_3 = index_3_stack.pop() + 1
                continue
        '''
        # dp[i][j]��ʾs3[i + j - 1]�Ƿ�����s1[i - 1]��s2[j - 1]��ɵ�
        dp = [[True for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]

        # �ֱ��¼s1��s2��s3���������ֵ����
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        # s1��ǰi���ַ���s2��ǰj���ַ��Ľ�������Ƿ���s3�г���
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
#coding:gb2312
'''
leetcode: Restore IP Addresses
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []

        start = 0 # ��ʾ��ʼ��λ��
        result = [] # �洢���

        if s[start] == '0': # �����0��ͷ,��ö���ֻ����0
            self.isIpAddresses(s, s[0:1] + ".", 1, 1, result)
        else:
            # ��1��3�����öεĳ���
            for i in range(1, 4):
                if int(s[start:start + i]) < 256:
                    self.isIpAddresses(s, s[start:start + i] + ".", start + i, 1, result)

        return result

    # temp_s��ʾ��ǰip��ַ,start��ʾ��ʼ������λ��,num��ʾ��ǰѰ�ҵĶεı��
    def isIpAddresses(self, s, temp_s, start, num, result):
        if num == 4 and start == len(s): # ����Ҫ��֤��ǰ�Ѿ�������s�Ľ�β
            result.append(temp_s[0:len(temp_s) - 1])
        elif num < 4:
            if start < len(s) and s[start] == '0':
                self.isIpAddresses(s, temp_s + s[start:start + 1] + ".", start + 1, num + 1, result)
            else:
                for i in range(1, 4):
                    if start + i <= len(s) and int(s[start:start + i]) < 256:
                        self.isIpAddresses(s, temp_s + s[start:start + i] + ".", start + i, num + 1, result)

if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("010010"))
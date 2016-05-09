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

        start = 0 # 表示开始的位置
        result = [] # 存储结果

        if s[start] == '0': # 如果以0开头,则该段里只能是0
            self.isIpAddresses(s, s[0:1] + ".", 1, 1, result)
        else:
            # 从1到3遍历该段的长度
            for i in range(1, 4):
                if int(s[start:start + i]) < 256:
                    self.isIpAddresses(s, s[start:start + i] + ".", start + i, 1, result)

        return result

    # temp_s表示当前ip地址,start表示开始搜索的位置,num表示当前寻找的段的编号
    def isIpAddresses(self, s, temp_s, start, num, result):
        if num == 4 and start == len(s): # 必须要保证当前已经搜索到s的结尾
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
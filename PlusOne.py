#coding:gb2312
'''
leetcode: Plue One
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if len(digits) == 0:
            return [1]

        jinwei = 0 #表示是否有进位发生

        #对digits进行加1操作
        if digits[-1] + 1 == 10:
            digits[-1] = 0
            jinwei = 1

            index = len(digits) - 2
            while index >= 0:
                if jinwei == 1 and digits[index] + 1 == 10:
                    digits[index] = 0
                elif jinwei == 1 and digits[index] + 1 < 10:
                    digits[index] += 1
                    jinwei = 0
                    break
                elif jinwei == 0:
                    break

                index -= 1

            #如果最高位有进位
            if index == -1 and jinwei == 1:
                digits[0] = 0
                digits = [1] + digits
        else:
            digits[-1] += 1

        return digits

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([9]))

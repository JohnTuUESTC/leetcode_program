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

        result = [] #保存返回的结果
        for i in range(len(digits)):
            result.append(0)

        jinwei = 0 #表示是否有进位发生

        #对digits进行加1操作
        if digits[len(digits) - 1] + 1 > 9:
            jinwei = 1
            result[len(digits) - 1] = (digits[len(digits) - 1] + 1) % 10

            #将进位的结果逐步向高位推进
            for i in range(len(digits) - 2, -1, -1):
                if jinwei == 1:
                    if digits[i] + 1 > 9:
                        result[i] = (digits[i] + 1) % 10
                    else:
                        result[i] = digits[i] + 1
                        jinwei = 0
                else:
                    result[i] = digits[i]

            if jinwei == 1:
                result = [1] + result
        else:
            result[len(digits) - 1] = digits[len(digits) - 1] + 1
            for i in range(len(digits) - 2, -1, -1):
                result[i] = digits[i]


        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([9]))

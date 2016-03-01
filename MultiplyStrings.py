#coding:gb2312
'''
leetcode: Multiply Strings
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num2 == "0":
            return "0"

        int_num1 = int(num1)
        result = 0

        list_num2 = list(num2)

        index = 0
        for i in range(len(num2) - 1, -1, -1):
            j = int(list_num2[i])
            temp_result = j * int_num1
            temp_result = temp_result * 10 ** index
            result += temp_result
            index += 1

        return str(result)

if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("123","12"))
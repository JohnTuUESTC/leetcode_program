#coding:gb2312
'''
leetcode: Pascal's Triangle II
'''

import copy

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        last_pascal_traingle_row = [1]
        pascal_traingle_row = [1]

        for i in range(1, rowIndex + 1):
            pascal_traingle_row = []
            for j in range(i + 1):
                pascal_traingle_row.append(0)

            for j in range(i + 1):
                if j - 1 < 0:
                    pascal_traingle_row[j] = last_pascal_traingle_row[j]
                elif j == len(last_pascal_traingle_row):
                    pascal_traingle_row[j] = last_pascal_traingle_row[j - 1]
                else:
                    pascal_traingle_row[j] = last_pascal_traingle_row[j]\
                    + last_pascal_traingle_row[j - 1]

            last_pascal_traingle_row = copy.deepcopy(pascal_traingle_row)

        return pascal_traingle_row

if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(3))
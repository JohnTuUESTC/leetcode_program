#coding:gb2312
'''
leetcode: Pascal's Triangle
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        pascal_triangle = [] #保存pascal三角

        for i in range(1, numRows + 1):
            temp = []
            for j in range(i):
                temp.append(0)
            pascal_triangle.append(temp)

        pascal_triangle[0][0] = 1

        for i in range(1, numRows):
            for j in range(i + 1):
                if j - 1 < 0:
                    pascal_triangle[i][j] = pascal_triangle[i - 1][j]
                elif j == len(pascal_triangle[i - 1]):
                    pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1]
                else:
                    pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1]\
                    + pascal_triangle[i - 1][j]

        return pascal_triangle

if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))


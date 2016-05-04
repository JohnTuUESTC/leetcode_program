#coding:gb2312
'''
leetcode: Maximal Rectangle
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        # 可以基于Largest Rectangle in Histogram	这个问题来解决
        # 将矩阵的一行作为输入

        heights = [0] * (len(matrix[0]) + 1) # 多加一个0作为参照值
        max_area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            '''
            max_area = max(max_area, self.getMax(heights, 0, len(heights)))

        return max_area

    def getMax(self, heights, first, last):
        if first + 1 == last:
            return heights[first]

        min_index = first  # 存储最小值的下标
        is_sorted = True  # 判断序列是否是有序的

        for i in range(first + 1, last):
            if heights[i] < heights[i - 1]:
                is_sorted = False
            if heights[i] < heights[min_index]:
                min_index = i

        # 如果中间某一段序列是有序的,可以避免递归
        if is_sorted:
            max_area = 0
            for i in range(first, last):
                max_area = max(max_area, heights[i] * (last - i))
            return max_area
        else:
            # 分别计算左右两侧的最大面积,再进行比较
            area_left = 0
            if min_index > first:
                area_left = self.getMax(heights, first, min_index)

            area_right = 0
            if min_index < last - 1:
                area_right = self.getMax(heights, min_index + 1, last)

            return max(heights[min_index] * (last - first), max(area_left, area_right))
        '''

            stack = [-1] # stack中存储数值增长序列的index, 由于heights的末尾多添加了一个0,所以该栈不会为空

            for j in range(len(matrix[0]) + 1):
                # 如果出现下降的情况,则将栈中的数据弹出,计算区域的最大值
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - 1 - stack[-1]
                    max_area = max(max_area, h * w)
                stack.append(j)
        return max_area

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalRectangle(["1"]))

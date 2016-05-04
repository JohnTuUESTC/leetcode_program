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

        # ���Ի���Largest Rectangle in Histogram	������������
        # �������һ����Ϊ����

        heights = [0] * (len(matrix[0]) + 1) # ���һ��0��Ϊ����ֵ
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

        min_index = first  # �洢��Сֵ���±�
        is_sorted = True  # �ж������Ƿ��������

        for i in range(first + 1, last):
            if heights[i] < heights[i - 1]:
                is_sorted = False
            if heights[i] < heights[min_index]:
                min_index = i

        # ����м�ĳһ�������������,���Ա���ݹ�
        if is_sorted:
            max_area = 0
            for i in range(first, last):
                max_area = max(max_area, heights[i] * (last - i))
            return max_area
        else:
            # �ֱ�������������������,�ٽ��бȽ�
            area_left = 0
            if min_index > first:
                area_left = self.getMax(heights, first, min_index)

            area_right = 0
            if min_index < last - 1:
                area_right = self.getMax(heights, min_index + 1, last)

            return max(heights[min_index] * (last - first), max(area_left, area_right))
        '''

            stack = [-1] # stack�д洢��ֵ�������е�index, ����heights��ĩβ�������һ��0,���Ը�ջ����Ϊ��

            for j in range(len(matrix[0]) + 1):
                # ��������½������,��ջ�е����ݵ���,������������ֵ
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - 1 - stack[-1]
                    max_area = max(max_area, h * w)
                stack.append(j)
        return max_area

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalRectangle(["1"]))

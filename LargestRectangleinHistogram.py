#coding:gb2312
'''
leetcode: Largest Rectangle in Histogram
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        TLE
        if len(heights) == 0:
            return 0
        elif len(heights) == 1:
            return heights[0]
        elif len(heights) == 2:
            return min(heights[0], heights[1]) * 2

        min_value = min(heights)
        min_index = heights.index(min_value)

        area_all = min_value * len(heights)
        area_left = self.largestRectangleArea(heights[0:min_index])
        area_right = self.largestRectangleArea(heights[min_index + 1:len(heights)])

        return max(area_all, max(area_left, area_right))
        '''

        if len(heights) == 0:
            return 0

        return self.getMax(heights, 0, len(heights))

    def getMax(self, heights, first, last):
        if first + 1 == last:
            return heights[first]

        min_index = first # �洢��Сֵ���±�
        is_sorted = True # �ж������Ƿ��������

        for i in range(first + 1, last):
            if heights[i] < heights[i - 1]:
                is_sorted = False
            if heights[i] < heights[min_index]:
                min_index = i

        #����м�ĳһ�������������,���Ա���ݹ�
        if is_sorted:
            max_area = 0
            for i in range(first, last):
                max_area = max(max_area, heights[i] * (last - i))
            return max_area
        else:
            #�ֱ�������������������,�ٽ��бȽ�
            area_left = 0
            if min_index > first:
                area_left = self.getMax(heights, first, min_index)

            area_right = 0
            if min_index < last - 1:
                area_right = self.getMax(heights, min_index + 1, last)

            return max(heights[min_index] * (last - first), max(area_left, area_right))


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))



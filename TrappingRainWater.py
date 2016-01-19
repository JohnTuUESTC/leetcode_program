# coding:gb2312
'''
leetcode: Trapping Rain Water
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 0 or len(height) == 1:
            return 0

        volumn = 0 # 记录存储水的体积
        max_height = height[0] # 记录最大高度
        max_height_index = 0 # 记录最大高度的位置

        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i

        # 从两端向最高高度,计算存水的体积
        temp_height = height[0] #记录当前遇到的最高高度
        for i in range(1, max_height_index):
            if temp_height > height[i]:
                volumn += temp_height - height[i]
            else:
                temp_height = height[i]

        temp_height = height[len(height) - 1]
        for i in range(len(height) - 2, max_height_index, -1):
            if temp_height > height[i]:
                volumn += temp_height - height[i]
            else:
                temp_height = height[i]

        return volumn

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([5,4,1,2]))




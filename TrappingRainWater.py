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

        volumn = 0 # ��¼�洢ˮ�����
        max_height = height[0] # ��¼���߶�
        max_height_index = 0 # ��¼���߶ȵ�λ��

        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i

        # ����������߸߶�,�����ˮ�����
        temp_height = height[0] #��¼��ǰ��������߸߶�
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




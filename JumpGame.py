#coding: gb2312
'''
leetcode: Jump Game
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        if len(nums) == 0:
            return True

        longest = [0] * len(nums) # ��¼�±��ܵ������Զλ��
        longest[0] = nums[0]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if longest[i] >= j:
                    longest[i] = max(nums[j] + j, longest[i])
                    longest[j] = nums[j] + j

        #print(longest)
        if max(longest) >= len(nums):
            return True
        else:
            return False
        '''
        if len(nums) == 0 or len(nums) == 1:
            return True

        index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # ����ϣ��һ���Ե��ƶ�̫��λ��, ÿ���ƶ���С��λ��
            if i + nums[i] >= index:
                index = i

        if index == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([3,2,1,0,4]))

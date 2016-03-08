#coding:gb2312
'''
leetcode: 3 Sum
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        target = 0 #��ʾĿ��ֵ

        result = [] #�洢���صĽ��

        nums.sort()

        for i in range(len(nums)):
            target -= nums[i]
            temp_nums = nums[i + 1:len(nums)] #����ֻ���i�����
            temp_result = self.twoSum(temp_nums, target)

            target += nums[i]
            for j in temp_result:
                j.append(nums[i])
                j.sort()
                if j not in result:
                    result.append(j)

        return result

    def twoSum(self, nums, target):
        '''
        :param nums:List[int]
        :param target:int
        :return:List[int]
        '''

        return_index = [] #���巵��ֵ
        visited_item = {} #���ֵ�洢�Ѿ���������Ԫ��, �Լӿ��������ٶ�

        #�ж�����ĳ����Ƿ�С��1
        if len(nums) <= 1:
            return return_index

        for i in range(len(nums)):
            if (target - nums[i]) in visited_item:
                temp = []
                temp.append(nums[visited_item[target - nums[i]]])
                temp.append(nums[i])
                return_index.append(temp)
            else:
                visited_item[nums[i]] = i

        return return_index

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
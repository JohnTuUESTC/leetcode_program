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

        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]: # ˵��������Ѿ���֮ǰ���ֹ���
                continue

            target -= nums[i]

            first = i + 1
            last = len(nums) - 1
            temp_result = []

            while first < last:
                while i + 1 < first <= len(nums) - 1 and nums[first] == nums[first - 1]:
                    first += 1

                while 0 <= last < len(nums) - 1 and nums[last] == nums[last + 1]:
                    last -= 1

                if first < last:
                    temp = nums[first] + nums[last]
                    if temp > target:
                        last -= 1
                    elif temp < target:
                        first += 1
                    else:
                        temp_list = []
                        temp_list.append(nums[i])
                        temp_list.append(nums[first])
                        temp_list.append(nums[last])
                        result.append(temp_list)
                        first += 1
                        last -= 1

            target += nums[i]

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([0,0,0]))
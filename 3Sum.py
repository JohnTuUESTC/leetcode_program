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

        target = 0 # 表示目标值

        result = [] # 存储返回的结果

        nums.sort()

        for i in range(0, len(nums) - 2):
            if nums[i] > 0: # 当一个数为正数时,如果有解的话,应该已经在负数中出现过了
                break

            if i > 0 and nums[i] == nums[i - 1]: # 除去重复
                continue

            target -= nums[i]

            first = i + 1
            last = len(nums) - 1

            while first < last:
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
                    # 去除重复值, 只有在得到一个解的时候才需要这个操作
                    while first < last and nums[first] == nums[first + 1]:
                        first += 1

                    while first < last and nums[last] == nums[last - 1]:
                        last -= 1

                    first += 1
                    last -= 1

            target += nums[i]

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([0,0,0]))
#coding:gb2312
'''
leetcode: Summary Ranges
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        first_index = 0
        last_index = 1
        first_num_index = 0 #表示开始的数字
        result = [] #返回结果

        while last_index < len(nums):
            if nums[last_index] - nums[first_index] != 1:
                if first_index == first_num_index: #如果连续的数字只有一个
                    result.append(str(nums[first_index]))
                else:
                    result.append(str(nums[first_num_index]) + "->" + str(nums[first_index]))

                first_num_index = first_index + 1

            first_index += 1
            last_index += 1

        if first_index == first_num_index:
            result.append(str(nums[first_index]))
        else:
            result.append(str(nums[first_num_index]) + "->" + str(nums[first_index]))

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
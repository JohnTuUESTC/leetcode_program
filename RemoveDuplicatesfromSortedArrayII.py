#coding:gb2312
'''
leetcode: Remove Duplicates from Sorted Array II
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        first = 0
        last = 1

        length = 0 # 返回列表的长度
        duplicated = False # 表示当前是否有重复元素

        while last < len(nums) - length:
            if nums[first] == nums[last + length]: # 表示当前已出现了重复的元素
                if duplicated:
                    length += 1
                else:
                    # 如果只出现了一个重复的元素
                    duplicated = True
                    nums[last] = nums[last + length]
                    first += 1
                    last += 1

            else:
                duplicated = False
                # 将不重复的元素复制到前面
                nums[last] = nums[last + length]
                first += 1
                last += 1

        return len(nums) - length

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))



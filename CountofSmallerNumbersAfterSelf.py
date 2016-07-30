#coding:utf-8
'''
leetcode: Count of Smaller Numbers After Self
'''

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]

        ret = [0] * len(nums)

        # 参数list(enumerate(nums))表示,记录元素以及其下标
        self.CountSmaller(list(enumerate(nums)), ret)

        return ret

    def CountSmaller(self, nums, smaller):
        mid = len(nums) / 2

        if mid:
            left = self.CountSmaller(nums[:mid], smaller)
            right = self.CountSmaller(nums[mid:], smaller)

            # 对数组按元素大小进行重新排序,相当于合并两个有序的数组
            for i in range(len(nums) - 1, -1, -1):
                # 如果左边数组的最后一个元素要比右边数组的最后一个元素大,逆序对数为右边数组的长度
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    nums[i] = left.pop()
                else:
                    nums[i] = right.pop()

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))

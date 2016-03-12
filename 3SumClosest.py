#coding:gb2312
'''
leetcode: 3 Sum Closest
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) <= 3:
            return sum(nums)

        nums.sort()

        first = 0
        last = len(nums) - 1
        closest_target = 0 #存储与目标值最接近的和
        target_distance = 1000

        target -= nums[first] + nums[last]

        while first < last - 1: #保证两者之间有三个元素
            #寻找当前最接近的解
            index = self.find_the_last(nums, first, last, target)
            if abs(target - nums[index]) < target_distance:
                closest_target = nums[first] + nums[last] + nums[index]
                target_distance = abs(target - nums[index])

            #根据当前的目标值,判断移动的方向
            if target - nums[index] > 0:
                if nums[first] - nums[first + 1] <= nums[last] - nums[last - 1]:
                    target += nums[first]
                    first += 1
                    target -= nums[first]
                else:
                    target += nums[last]
                    last -= 1
                    target -= nums[last]
            else:
                if nums[first] - nums[first + 1] >= nums[last] - nums[last - 1]:
                    target += nums[first]
                    first += 1
                    target -= nums[first]
                else:
                    target += nums[last]
                    last -= 1
                    target -= nums[last]

        return closest_target

    def find_the_last(self, nums, first, last, target):
        if target > 0:
            i = last - 1
            min_target = abs(target - nums[i])
            min_index = i
            i -= 1
            while i > first and nums[i] > 0:
                if abs(target - nums[i]) <= min_target:
                    min_target = abs(target - nums[i])
                    min_index = i
                i -= 1

            i -= 1
            if i > first and abs(target - nums[i]) <= min_target:
                min_target = abs(target - nums[i])
                min_index = i

            return min_index
        else:
            i = first + 1
            min_target = abs(target - nums[i])
            min_index = i
            i += 1
            while i < last and nums[i] < 0:
                if abs(target - nums[i]) <= min_target:
                    min_target = abs(target - nums[i])
                    min_index = i

                i += 1

            i += 1
            if i < last and abs(target - nums[i]) <= min_target:
                min_target = abs(target - nums[i])
                min_index = i

            return min_index

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))

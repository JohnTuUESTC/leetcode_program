#coding:gb2312
'''
leetcode: Insert Interval
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return [newInterval]

        if newInterval.end < intervals[0].start:
            return [newInterval] + intervals

        if newInterval.start > intervals[len(intervals) - 1].end:
            return intervals + [newInterval]

        first = 0
        last = len(intervals) - 1

        # 寻找到新区间应该插入的首尾位置
        while first < len(intervals):
            if newInterval.start < intervals[first].start:
                break
            elif intervals[first].start <= newInterval.start <= intervals[first].end:
                break

            first += 1

        while last > -1:
            if intervals[last].end < newInterval.end:
                break
            elif intervals[last].start <= newInterval.end <= intervals[last].end:
                break

            last -= 1

        # 构造新的区间
        new_interval = Interval()
        new_interval.start = min(intervals[first].start, newInterval.start)
        new_interval.end = max(intervals[last].end, newInterval.end)

        result_interval = intervals[0:first] + [new_interval] + intervals[last + 1:len(intervals)]

        return result_interval

if __name__ == "__main__":
    interval_1 = Interval(1, 2)
    interval_2 = Interval(3, 5)
    interval_3 = Interval(6, 7)
    interval_4 = Interval(8, 10)
    interval_5 = Interval(12, 16)
    interval_6 = Interval(4, 9)


    sol = Solution()
    print(sol.insert([interval_1, interval_2,interval_3,interval_4,interval_5], interval_6))
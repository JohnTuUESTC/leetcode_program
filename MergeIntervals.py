#coding:gb2312
'''
leetcode: Merge Intervals
'''

class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        #按区间的开始从大到小进行排序
        self.sort_intervals(intervals, 0, len(intervals) - 1)

        result = []
        result.append(intervals[0])

        for j in range(1, len(intervals)):
            #判断两个区间是否有交集
            if self.interval_overlapped(intervals[j], result[len(result) - 1]):
                #将相交的区间进行合并
                new_inter = self.merge_interval(intervals[j], result[len(result) - 1])
                result.pop()
                result.append(new_inter)
            else:
                result.append(intervals[j])

        return result

    def sort_intervals(self, intervals, start, end):
        if start >= end:
            return

        target = intervals[end]

        j = start - 1
        i = start

        while i < end:
            if intervals[i].start < target.start:
                j += 1
                temp = intervals[i]
                intervals[i] = intervals[j]
                intervals[j] = temp
            i += 1

        j += 1
        intervals[end] = intervals[j]
        intervals[j] = target
        self.sort_intervals(intervals, 0, j - 1)
        self.sort_intervals(intervals, j + 1, end)

    def interval_overlapped(self, interval_1, interval_2):
        if interval_1.start > interval_2.start:
            return self.interval_overlapped(interval_2, interval_1)

        if interval_1.start <= interval_2.start <= interval_1.end:
            return True

    def merge_interval(self, interval_1, interval_2):
        new_interval = Interval()

        new_interval.start = min(interval_1.start, interval_2.start)
        new_interval.end = max(interval_1.end, interval_2.end)

        return new_interval

if __name__ == "__main__":
    interval = []
    interval.append(Interval(2,3))
    interval.append(Interval(4,5))
    interval.append(Interval(6,7))
    interval.append(Interval(8,9))
    interval.append(Interval(1,10))

    sol = Solution()
    new = sol.merge(interval)

    for i in range(len(new)):
        print("("),
        print(new[i].start),
        print(", "),
        print(new[i].end),
        print(")")

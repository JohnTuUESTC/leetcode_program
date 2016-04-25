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

        #按区间的起始从小到大进行排序
        intervals = sorted(intervals, key=lambda x: x.start)

        result = []
        result.append(intervals[0])

        for j in range(1, len(intervals)):
            #判断两个区间是否有交集
            if intervals[j].start <= result[-1].end:
                result[-1].end = max(intervals[j].end, result[-1].end)
            else:
                result.append(intervals[j])

        return result


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

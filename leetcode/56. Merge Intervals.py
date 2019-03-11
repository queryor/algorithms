# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        #34%
        i = 0
        intervals.sort(key=lambda i:i.start)
        while i <len(intervals)-1:
            s1,s2 = intervals[i].start,intervals[i+1].start
            e1,e2 = intervals[i].end,intervals[i+1].end
            if e1>=s2:
                intervals[i].end = max(e1,e2)
                intervals.pop(i+1)
            else:
                i+=1
        return intervals
    def merge1(self, intervals):
        # 76%
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

s = Solution() 
i = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
print(s.merge(i))
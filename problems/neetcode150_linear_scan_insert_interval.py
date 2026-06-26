# Problem: Insert Interval  (NeetCode 150)
#
# You are given an array of non-overlapping intervals `intervals` where
# intervals[i] = [start_i, end_i] represents the start and end of the ith
# interval. `intervals` is initially sorted in ascending order by start_i.
#
# You are given another interval newInterval = [start, end].
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by start_i and still has no overlapping intervals (merge
# overlapping intervals if needed). Return intervals after adding newInterval.
#
# Note: Intervals are non-overlapping if they have no common point. For example,
# [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.
#
# Example 1:
#   Input:  intervals = [[1,3],[4,6]], newInterval = [2,5]
#   Output: [[1,6]]
#   Explanation: [2,5] overlaps with [1,3] and [4,6], so all three merge into [1,6].
#
# Example 2:
#   Input:  intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
#   Output: [[1,2],[3,5],[6,7],[9,10]]
#   Explanation: [6,7] does not overlap with any existing interval, so it is
#                simply inserted between [3,5] and [9,10].
#
# Constraints:
#   0 <= intervals.length <= 1000
#   newInterval.length == intervals[i].length == 2
#   0 <= start <= end <= 1000

from typing import List


# ============================================================
# Approach 1 (OPTIMAL): Linear scan / greedy merge  —  O(n) time, O(n) space
# ============================================================
# Since the input is already sorted by start, a single left-to-right pass in
# three phases suffices. This is optimal: every interval must be inspected at
# least once, so O(n) time is the lower bound. The O(n) space is just the output
# list (O(1) auxiliary beyond it).
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        # phase 1: intervals ending before newInterval starts
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1
        # phase 2: merge all that overlap (start at/before newInterval's end)
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        res.append(newInterval)
        # phase 3: the rest
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1
        return res

# Problem: Merge Intervals  (NeetCode 150)
# Difficulty: Medium
#
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all
# overlapping intervals, and return an array of the non-overlapping intervals that
# cover all the intervals in the input.
#
# You may return the answer in any order.
#
# Note: Intervals are non-overlapping if they have no common point. For example,
# [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.
#
# Example 1:
#   Input:  intervals = [[1,3],[1,5],[6,7]]
#   Output: [[1,5],[6,7]]
#
# Example 2:
#   Input:  intervals = [[1,2],[2,3]]
#   Output: [[1,3]]
#
# Constraints:
#   1 <= intervals.length <= 1000
#   intervals[i].length == 2
#   0 <= start <= end <= 1000

from typing import List


# ============================================================
# Approach 1 (OPTIMAL): Sort + linear merge  —  O(n log n) time, O(n) space
# ============================================================
# Sort by start, then sweep once. For each interval, while the last interval in
# res overlaps (res[-1][1] >= interval[0]), pop it and expand the current interval
# to cover both, then append. Because the input is sorted by start, each interval
# only ever needs to merge with the most recent one in res, so the inner while runs
# O(1) amortized and the sweep is O(n). The O(n log n) sort dominates — that's the
# optimal bound here, since merging fundamentally requires the intervals ordered.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []

        res=[]
        intervals.sort()

        for interval in intervals:
            while res and res[-1][1]>=interval[0]:
                interval[0]=min(res[-1][0],interval[0])
                interval[1]= max(res[-1][1],interval[1])
                res.pop()

            res.append(interval)

        return res

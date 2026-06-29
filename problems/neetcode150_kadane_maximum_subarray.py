# Problem: Maximum Subarray  (NeetCode 150)
# Difficulty: Medium
#
# Given an array of integers nums, find the subarray with the largest sum and
# return the sum. A subarray is a contiguous non-empty sequence of elements.
#
# Example 1:
#   Input:  nums = [2,-3,4,-2,2,1,-1,4]
#   Output: 8
#   Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.
#
# Example 2:
#   Input:  nums = [-1]
#   Output: -1
#
# Constraints:
#   1 <= nums.length <= 1000
#   -1000 <= nums[i] <= 1000

from typing import List


# ============================================================
# Approach 1 (OPTIMAL): Kadane's algorithm  —  O(n) time, O(1) space
# ============================================================
# Sweep once, keeping a running sum curSum. At each element, if extending the
# current run is worse than starting fresh at num (curSum < num), restart the run
# at num; otherwise keep extending. Track the best sum seen. The extra start /
# bestStart / bestEnd bookkeeping isn't needed for the answer but recovers the
# actual subarray (nums[bestStart : bestEnd + 1]). A single linear pass with O(1)
# state is optimal — you must look at every element at least once.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0
        start = 0                       # tentative start of current run
        bestStart, bestEnd = 0, 0
        for i, num in enumerate(nums):
            curSum = curSum + num
            if curSum < num:            # restart the run at i
                curSum = num
                start = i               # tentative start moves here
            if curSum > maxSum:         # new best → commit the window
                maxSum = curSum
                bestStart = start       # lock in the floating start
                bestEnd = i
        return maxSum                   # subarray is nums[bestStart : bestEnd + 1]

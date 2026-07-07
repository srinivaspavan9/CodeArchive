# 329. Longest Increasing Path in a Matrix
# Solved
# Hard
# Topics
# conpanies iconCompanies

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:

# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Example 3:

# Input: matrix = [[1]]
# Output: 1

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 200
#     0 <= matrix[i][j] <= 231 - 1

#  


from typing import List
from collections import defaultdict


# ============================================================
# Approach (OPTIMAL): DFS + memoization (top-down DP on the DAG)
#   —  O(m*n) time, O(m*n) space
# ============================================================
# View cells as a DAG with edges pointing to strictly-greater neighbors.
# maxLength(r,c) = longest increasing path starting at (r,c) = 1 + max over those
# greater neighbors; memoize so each cell is solved once. Answer = max over all
# start cells. m*n cells, O(1) work (4 dirs) each => O(m*n) time and O(m*n) memo
# space — optimal for this problem.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        memo = defaultdict(int)
        maxLen =0

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        def maxLength(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            best=0
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n  and matrix[nr][nc]>matrix[r][c]:
                    best = max(best,maxLength(nr,nc))
            memo[(r,c)]=1+best
            return memo[(r,c)]
        
        for i in range(m):
            for j in range(n):
                maxLen=max(maxLen,maxLength(i,j))
        
        return maxLen
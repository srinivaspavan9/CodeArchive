# Problem: Maximum Score Stone Jumps
# Status: SOLVED
#
# You are given a sequence of stones, each represented by a non-negative integer. Your task is to calculate the 
# maximum possible score by jumping from the beginning of the sequence to the end.

# The rules for jumping and scoring are as follows:


# Starting Point:


# Always start at the first stone (index 0).

# The value of the first stone does not contribute to the score as you jump from it.

# Jumping Rules:


# From the current stone at index i, you can jump to any stone at a higher index j (j > i).

# The number of positions you jump is calculated as jump_distance = j - i.



# Scoring Mechanism:



# Each jump contributes to your total score based on the destination stone's value and the number of positions jumped.

# For a jump from stone i to stone j, the score contribution is:

# score = stones[j] * jump_distance

# Total Score: The sum of all individual jump scores from the start to the end.

# Objective:



# Determine the sequence of jumps that maximizes the total score.



# [1,2,3....10, 0, 16]

# 0 1 2         5   6



# 0 -> 1 -> 2 

# 0 -> 2

# ...



# 0-> 1 : (1 - 0) * 2 = 2 

# 1 -> 2 : (2 - 1) * 3 = 3

# sum: 5

# THis was my initail approach 


# function (start_idx, stones,curent_Score, max_score ):

#     boundary condition : where we reach the last stone:

#         we compare the current reached socre with the max_score :

#             if greater we update the max_score

        

#     for i in rang(from start_ids to end):

#         we choose the ith stone :

#             upadate the current score 

#             function(i,add up the score , max_score)

#             reset the current score 





# memoize -> cache


# ============================================================
# Approach 1: Top-down DP (memoized recursion)  —  O(n^2) time, O(n) space
# ============================================================
# getMaxScore(idx) = best score to reach idx = max over i<idx of
# getMaxScore(i) + (idx-i)*stones[idx]. Correct, but the inner loop over every
# i<idx makes it O(n^2) (plus O(n) recursion depth). NOTE: the "# dp - O(n)"
# label further down is inaccurate — both DP solutions here are O(n^2), not O(n).
def maxScoreStoneJumps(stones):
    if not stones:
        return 0
    n = len(stones)
    memo = [float('-inf')] * n  

    def getMaxScore(idx):
        if memo[idx] != float('-inf'):    
            return memo[idx]
        if idx == 0:
            memo[idx] = 0
            return 0
        for i in range(idx):
            memo[idx] = max(memo[idx], getMaxScore(i) + (idx - i) * stones[idx])
        return memo[idx]

    return getMaxScore(n - 1)


# ============================================================
# Approach 2: Bottom-up DP  —  O(n^2) time, O(n) space
# ============================================================
# dp[j] = max over i<j of dp[i] + (j-i)*stones[j]. Cleaner than approach 1 (no
# recursion), but the same complexity. The "# dp - O(n)" label just below is
# wrong: the nested i-loop makes this O(n^2). The genuine O(n log n) optimum is
# described in the AI notes at the end of the file.

# dp - O(n)

# THis is my second approach

# dp[i] -> max score to reach ith index
# so then that makes dp[j]= max(dp[i]+(j-i)*stones[j]) where i : 0->j-1



def maxScoreStoneJumps(stones):
	if not stones:
		return 0

	n=len(stones)
	dp=[0]*n
	dp[0]=0

	for j in range(1,n):
		for i in range(0,j):
			dp[j]=max(dp[j],dp[i]+stones[j]*(j-i))

	return dp[n-1]


# ================== AI (Claude) NOTES — START ==================
# (Hints only — no code on purpose, so you can implement it yourself on revision.)
# FASTER APPROACH: Convex Hull Trick / Li Chao tree  —  O(n log n) time, O(n) space
# ===============================================================
# Both DP solutions above are O(n^2). You can get below that by noticing the
# recurrence is a max over straight lines:
#
#   dp[j] = max_{i<j} ( dp[i] + (j - i) * stones[j] )
#         = j*stones[j] + max_{i<j} ( dp[i] - i*stones[j] )
#
# Read that inner max as: each earlier index i defines a LINE
#       f_i(x) = (-i) * x + dp[i]        (slope = -i, intercept = dp[i])
# and for index j you evaluate every such line at the single point x = stones[j]
# and take the maximum. So dp[j] = j*stones[j] + (best line value at x=stones[j]).
#
# The whole job becomes: "keep a set of lines, support (a) add a line, and
# (b) ask for the max value of any line at a given x." That's exactly what the
# Convex Hull Trick answers. The set of lines forms an upper envelope; querying
# the best line at a point is O(log n).
#
# Implementation hints (so you can build it from scratch):
#   - Process j = 0, 1, ..., n-1 in order. Before computing dp[j], all lines for
#     i < j are already inserted, so a query at x = stones[j] is valid.
#   - A Li Chao tree (segment-tree-like, keyed on the x range [0 .. max(stones)])
#     is the easiest correct structure: each node stores the line that's best at
#     its midpoint, and you recurse left/right to fix the rest. Both insert and
#     query are O(log V).
#   - Alternatively, since the slopes -i are added in strictly decreasing order,
#     a monotonic-deque CHT works too, with a binary search per query → O(n log n).
#   - Sanity check while coding: it must produce the SAME dp values as Approach 2
#     above — only the way you compute the inner max changes.
# =================== AI (Claude) NOTES — END ===================



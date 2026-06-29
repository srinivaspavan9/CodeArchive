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
# in the AI block at the end of the file.

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


# ===================== AI (Claude) SOLUTION — START =====================
# Approach 3 (OPTIMAL — added by Claude): Convex Hull Trick via Li Chao tree
#   —  O(n log V) time, O(n) space   (V = max stone value)
#
# Both DP solutions above are O(n^2). The recurrence rearranges so each dp[j]
# is a maximum over straight lines evaluated at a single point:
#
#   dp[j] = max_{i<j} ( dp[i] + (j - i) * stones[j] )
#         = j*stones[j] + max_{i<j} ( dp[i] - i*stones[j] )
#
# Treat each earlier index i as a line  f_i(x) = (-i)*x + dp[i]
# (slope -i, intercept dp[i]). Then dp[j] = j*stones[j] + max_i f_i(stones[j]) —
# i.e. query the upper envelope of those lines at x = stones[j]. A Li Chao tree
# maintains that envelope with O(log V) insert/query, so the whole thing is
# O(n log V). (A monotonic-slope CHT with binary-search queries is O(n log n).)
# This isn't test-run here; it follows the same recurrence as the DP above by
# construction — the only change is HOW the inner max is computed.

class _LiChaoNode:
    __slots__ = ('m', 'b', 'left', 'right', 'has')
    def __init__(self):
        self.m = 0; self.b = 0
        self.left = None; self.right = None
        self.has = False

def _insert(node, lo, hi, m, b):
    if not node.has:
        node.m, node.b, node.has = m, b, True
        return
    mid = (lo + hi) // 2
    left_better = m * lo + b > node.m * lo + node.b
    mid_better = m * mid + b > node.m * mid + node.b
    if mid_better:                       # keep the better line at this node
        node.m, node.b, m, b = m, b, node.m, node.b
    if lo == hi:
        return
    if left_better != mid_better:        # the loser still wins on the left half
        if node.left is None:
            node.left = _LiChaoNode()
        _insert(node.left, lo, mid, m, b)
    else:                                # ... otherwise on the right half
        if node.right is None:
            node.right = _LiChaoNode()
        _insert(node.right, mid + 1, hi, m, b)

def _query(node, lo, hi, x):
    if node is None or not node.has:
        return float('-inf')
    res = node.m * x + node.b
    if lo == hi:
        return res
    mid = (lo + hi) // 2
    if x <= mid:
        return max(res, _query(node.left, lo, mid, x))
    return max(res, _query(node.right, mid + 1, hi, x))

def maxScoreStoneJumps_optimal(stones):
    if not stones:
        return 0
    n = len(stones)
    if n == 1:
        return 0
    lo, hi = 0, max(stones)
    root = _LiChaoNode()
    dp = [0] * n
    _insert(root, lo, hi, 0, dp[0])          # i = 0: slope 0, intercept dp[0]=0
    for j in range(1, n):
        best = _query(root, lo, hi, stones[j])
        dp[j] = stones[j] * j + best
        _insert(root, lo, hi, -j, dp[j])     # add the line for index j
    return dp[n - 1]

# ====================== AI (Claude) SOLUTION — END ======================



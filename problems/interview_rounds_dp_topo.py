
# ============================================================
# Interview writeup — multiple rounds, kept together as one file
# ------------------------------------------------------------
#   Telephone screen : Max score take/skip jumps ..... SOLVED (DP)
#   Onsite round 1   : Android phone patterns ........ NOT SOLVED (unclear)
#   Onsite round 2   : Task completion time .......... NOT SOLVED (unclear)
#   Onsite round 3   : Play songs in valid order ..... SOLVED (topological sort)
# ============================================================


# Telephone screening round : 
# Given an array of positive elements, you can start at any element, at every element
# you have a choice to take it or skip it.
# If you take it the score will be increased by arr[i] and your next position will be i + arr[i],
# we have to find the max score that we can get



# given input  arr[] 

# dp[i] -> max score ending at that index
# dp[i] = max(dp[i-1], dp[i-arr[k]]+ arr[k])

# ============================================================
# Telephone round — Approach: DP over reachable landings  —  O(n^2) time, O(n) space
# ============================================================
# dp[i] = best score to reach index i: either from i-1 (skip) or from some j with
# j+arr[j]==i (took the jump at j, +arr[j]); answer = max dp[i]. BUG as written:
# the `dp[i]=max(dp[i-1],...)` sits INSIDE `if i==j+arr[j]`, so any index that no
# jump lands on never inherits dp[i-1] (stays 0) — move the skip-carry outside the
# j-loop's if. (The rules were a bit ambiguous: what "skip" advances to, and
# whether a jump landing past the end still scores.)
def getMaxScore(arr):
	n=len(arr)
	dp=[0]*n
	max_score = float("-inf")
	for i in range(1,n):
		for j in range(0,i):
			if i==j+arr[j]:
				dp[i]=max(dp[i-1],dp[j]+arr[j],dp[i])
		max_score = max(dp[i],max_score)
	return max_score


# ================== AI (Claude) NOTES — START ==================
# (Hints only — no code, so you can redo it yourself.)
# FASTER: this DP can be O(n) instead of O(n^2). Don't scan all j<i to find who
# lands on i — push forward. Walk i left->right keeping dp[i], relax the landing
# dp[i+arr[i]] = max(dp[i+arr[i]], dp[i]+arr[i]) (bounds-check it), and carry skips
# with dp[i] = max(dp[i], dp[i-1]). One pass => O(n) time, O(n) space. (First pin
# down the exact rules noted in the bug comment above — they change the boundary.)
# =================== AI (Claude) NOTES — END ===================








# Onsite round 1 : 
# Android phone patterns : Given n,m which are a set of points, we have to find the total
# possible unique patterns that can be drawn, min len of a pattern is 1, n,m >=1

# Didnt properly understand the above question 


# Onsite round 2 : Find task completion time
# There will be some tasks, and each task can have one or more subtasks, by default all tasks have
# completion time 1 unit, but the comp_time of a parent task is the x if all subtasks have time x, 
# otherwise it is their sum, we have to find the total completion time

# Didnt properly understand the above question


# Onsite round 3 : Play songs in order
# There are n people and each person has a specific order in which the songs should be played,
# P1 : a,b,c
# P2. : b, e , f 
# We have to find if we can find a valid order, if there is a valid order we have to return that, 
# this is a topological ordering problem


# ============================================================
# Onsite round 3 — Approach: Topological sort (Kahn's BFS)  —  O(V + E) time/space
# ============================================================
# Build a DAG from each person's song order (edge between consecutive songs), then
# Kahn's algorithm: enqueue indegree-0 nodes, pop+append, decrement successors. If
# the output covers every node a valid order exists, else there's a cycle. Right
# (optimal) approach, but the code has bugs:
#   1) `queue.popLeft()` -> the deque method is `popleft()`.
#   2) Missing imports: `from collections import defaultdict, deque`.
#   3) Source-only songs (never a successor, e.g. the first in a list) never get
#      an indegree entry, so they're never enqueued and the final
#      len(validOrder)==len(indegree) check is off. Seed every node into indegree
#      (e.g. indegree[music[i]] += 0) and compare against the full node count.
def getValidOrder(musicList):
	graph=defaultdict(list)
	indegree = defaultdict(int)
	validOrder = []
	queue = deque()

	for music in musicList:
		for i in range(len(music)-1):
			graph[music[i]].append(music[i+1])
			indegree[music[i+1]]+=1

	for song in indegree:
		if indegree[song]==0:
			queue.append(song)

	while queue:
		curSong = queue.popLeft()
		validOrder.append(curSong)
		for nextSong in graph[curSong]:
			indegree[nextSong]-=1
			if indegree[nextSong]==0:
				queue.append(nextSong)

	if len(validOrder)==len(indegree):
		return validOrder
	return None


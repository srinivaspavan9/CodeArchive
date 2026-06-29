# Problem Context Index

Context lookup table for matching a problem the user describes to its file. The
description column is intentionally keyword-rich (the real-world subject of the problem)
so a vague mention ("the chess rank one") maps to the right file. Maintained on every
cleanup — one row per problem file.

| File | Context |
|------|---------|
| `problems/dfs_chess_tournament_ranks.py` | Chess tournament ranking problem. Given M games as [winner, loser] among N players (the higher-ranked player always wins), find which players' ranks can be precisely determined through transitive win/loss relationships. Solved with DFS over win/loss graphs counting transitive wins + losses; that DFS approach is the optimal one (O(n·(n+m))). |
| `problems/dynamic_programming_max_score_stone_jumps.py` | Jumping-stones max-score problem. Given a sequence of non-negative stone values, jump from index 0 to the end; a jump i→j scores stones[j]·(j−i), and you want to maximize the total. SOLVED with two DP approaches (top-down memoized + bottom-up), both O(n²) — the user's "O(n)" note was wrong. A faster O(n log n) convex hull trick / Li Chao optimum is described in AI-fenced notes (hints only, no code) since dp[j] = j·stones[j] + max over lines f_i(x)=−i·x+dp[i] at x=stones[j]. |
| `problems/neetcode150_linear_scan_insert_interval.py` | NeetCode 150 "Insert Interval" problem. Given a list of sorted, non-overlapping intervals and a new interval, insert it and merge any overlaps, keeping the list sorted. Solved with a single-pass three-phase linear scan / greedy merge (before / overlapping / after), which is optimal at O(n) time, O(n) space. |
| `problems/neetcode150_sorting_merge_intervals.py` | NeetCode 150 "Merge Intervals" problem. Given an array of (possibly unsorted, overlapping) intervals [start, end], merge all overlapping ones and return the non-overlapping cover. Solved by sorting on start then sweeping once, popping/expanding the last result interval whenever it overlaps the current one. Optimal at O(n log n) time, O(n) space (the sort dominates). |
| `problems/neetcode150_kadane_maximum_subarray.py` | NeetCode 150 "Maximum Subarray" problem. Given an integer array (with negatives), find the contiguous non-empty subarray with the largest sum and return that sum. Solved with Kadane's algorithm — one pass keeping a running sum that restarts whenever extending is worse than starting fresh, plus optional start/end index tracking to recover the actual window. Optimal at O(n) time, O(1) space. |

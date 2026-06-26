# Problem Context Index

Context lookup table for matching a problem the user describes to its file. The
description column is intentionally keyword-rich (the real-world subject of the problem)
so a vague mention ("the chess rank one") maps to the right file. Maintained on every
cleanup — one row per problem file.

| File | Context |
|------|---------|
| `problems/dfs_chess_tournament_ranks.py` | Chess tournament ranking problem. Given M games as [winner, loser] among N players (the higher-ranked player always wins), find which players' ranks can be precisely determined through transitive win/loss relationships. Solved with DFS over win/loss graphs counting transitive wins + losses; that DFS approach is the optimal one (O(n·(n+m))). |
| `problems/unsolved_max_score_stone_jumps.py` | Jumping-stones max-score problem. Given a sequence of non-negative stone values, jump from index 0 to the end; a jump i→j scores stones[j]·(j−i), and you want to maximize the total. UNSOLVED — question only; user is leaning toward a DP / memoized O(n) approach. |

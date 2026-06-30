# CodeArchive

Personal archive of coding problems I solve — kept so I don't forget them.

## Index

Click a file to jump straight to it. Status: ✅ Solved · ❌ Unsolved (question only, to do later).

| Problem | Status | Optimal approach | File |
|---------|--------|------------------|------|
| Chess tournament ranks | ✅ Solved | DFS | [dfs_chess_tournament_ranks.py](problems/dfs_chess_tournament_ranks.py) |
| Maximum score stone jumps | ✅ Solved | Dynamic programming | [dynamic_programming_max_score_stone_jumps.py](problems/dynamic_programming_max_score_stone_jumps.py) |
| Insert Interval (NeetCode 150) | ✅ Solved | Linear scan | [neetcode150_linear_scan_insert_interval.py](problems/neetcode150_linear_scan_insert_interval.py) |
| Merge Intervals (NeetCode 150) | ✅ Solved | Sort + linear merge | [neetcode150_sorting_merge_intervals.py](problems/neetcode150_sorting_merge_intervals.py) |
| Maximum Subarray (NeetCode 150) | ✅ Solved | Kadane's algorithm | [neetcode150_kadane_maximum_subarray.py](problems/neetcode150_kadane_maximum_subarray.py) |
| Number of islands in a tree | ✅ Solved | Union-Find (disjoint set) | [union_find_number_of_islands_in_tree.py](problems/union_find_number_of_islands_in_tree.py) |

## Layout

Everything lives flat in [`problems/`](problems/). The **filename is the structure**:

```
<optimal_approach>_<problem_context>.py
```

- `optimal_approach` — the best technique for the problem (`dynamic_programming`, `hashmap`, `dfs`, `two_pointers`, ...)
- `problem_context` — short name of the problem

Examples:

| File | Optimal approach | Problem |
|------|------------------|---------|
| `dynamic_programming_chess_games_problem.py` | Dynamic programming | Chess games |
| `hashmap_two_sum.py` | Hash map | Two Sum |
| `dfs_course_schedule.py` | DFS | Course Schedule |

Sorting the folder groups problems by technique. Each file starts with the problem
statement (as comments), followed by one or more approaches, each labeled with its
complexity.

## Workflow

1. Drop a new `.py` in `problems/` — problem statement at the top, then solution(s).
2. Filenames get normalized and approaches get labeled before committing.
3. Commit & push.

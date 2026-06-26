# CodeArchive

Personal archive of coding problems I solve — kept so I don't forget them.

## Index

Click a file to jump straight to it.

| Problem | Optimal approach | File |
|---------|------------------|------|
| Chess tournament ranks | DFS | [dfs_chess_tournament_ranks.py](problems/dfs_chess_tournament_ranks.py) |

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

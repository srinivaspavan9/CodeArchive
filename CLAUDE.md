# CodeArchive — Claude Instructions

Personal record-keeping repo for coding problems from a paid practice service.
The user solves a problem (usually in a day) and wants it cleanly archived so they
don't forget it. Keep everything **lightweight**. Do not over-engineer or add
boilerplate.

## ⛔ HARD RULE: never push, commit, or touch git/GitHub

All git operations — `git add`, `git commit`, `git push`, `gh`, remotes, branches —
are **the user's job, always**. Do not run them. Do not offer to run them. Do not
stage or commit "to help." Your job ends at cleaning the file and saying it's ready;
the user reviews and runs every git command themselves. This is non-negotiable even
if it seems convenient or the user is in a hurry.

## The user's workflow

1. The user creates a Python file in `problems/` with **any random name** and writes:
   - the problem statement at the top (inside comments), then
   - their solution code, possibly with multiple approaches.
   Their only focus is solving — the file may be messy or badly named.
2. The user tells you something like "added a new one" / "done this one" / "I finished a problem".
3. **You** clean it up (see below), then report it's ready and show the final name + a
   preview of the file.
4. The user confirms, then **the user** runs the git/push commands themselves.
   See the HARD RULE above — never run git/push yourself.

## What you do when a problem is added/finished

Look at new or changed files in `problems/` and, for each:

1. **Rename to the convention** (only if the current name isn't already intuitive/correct):

   ```
   <optimal_approach>_<problem_context>.py
   ```

   - all lowercase **snake_case**, single underscores between words.
   - `<optimal_approach>` = the *best/optimal* technique for the problem
     (e.g. `dynamic_programming`, `hashmap`, `dfs`, `two_pointers`, `binary_search`).
     Use this even if the file also contains a brute-force or other approaches inside —
     the filename advertises the optimal one.
   - `<problem_context>` = a short descriptive name of the problem
     (e.g. `chess_games_problem`, `two_sum`, `course_schedule`).
   - Examples: `dynamic_programming_chess_games_problem.py`, `hashmap_two_sum.py`,
     `dfs_course_schedule.py`.

2. **Tidy the problem statement** at the top (keep it as a comment block / docstring).
   Fix obvious formatting but preserve the user's wording. If a source link exists, keep it.

3. **Separate and label each approach** with a clear comment header, e.g.:

   ```python
   # ============================================================
   # Approach 1: Brute Force  —  O(n^2) time, O(1) space
   # ============================================================
   ```

   - One label per approach. State the technique name and time/space complexity.
   - Mark which one is optimal (matches the filename prefix).

4. **Do NOT rewrite the user's logic.** Only add comment labels, fix the header,
   and rename. Don't refactor working code unless asked.

5. **Report, don't push.** Tell the user the final filename and show how the file
   now looks. Wait for their confirmation. They handle git.

## File anatomy (target shape)

```python
# Problem: <name>
# Source: <link if any>
#
# <problem statement, cleaned but in the user's words>

# ============================================================
# Approach 1: <technique>  —  O(?) time, O(?) space
# ============================================================
def ...

# ============================================================
# Approach 2 (OPTIMAL): <technique>  —  O(?) time, O(?) space
# ============================================================
def ...
```

## Structure

- One folder: `problems/`. Everything lives flat inside it. Do not create subfolders.
- Root holds only `README.md`, `CLAUDE.md`, `.gitignore`.

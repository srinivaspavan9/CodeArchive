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

## Editing an existing file / adding a new approach

The user won't always add a brand-new problem — sometimes they **edit an existing file**,
e.g. "I edited a file", "added a new approach to that problem", or they just describe a
problem and say they changed it. You then do the cleanup for the changed file.

**You do NOT need the user to give the exact filename.** Figure out which file they mean:

1. **Consult `problem_context.md` first.** It's a keyword-rich context lookup table
   (file → 2-3 line description of the problem's real-world subject). Match the user's
   description ("the chess rank one") against the Context column to find candidate files,
   then **confirm the exact filename with the user** before editing.
2. If the context table doesn't resolve it, match against the actual files in `problems/`
   or find the **most recently modified** one (`ls -lt problems/`), open it, and confirm.
3. If it's still ambiguous (e.g. several files touched), **ask which one** before editing.

Use the context table, modification times, and file contents to detect changes — do **not**
lean on git for this (stay clear of the user's git workflow per the HARD RULE).

When a new approach was added to an existing file, on top of the normal cleanup below:

- **Re-judge optimality across ALL approaches now in the file**, not just the new one.
- If the newly added approach is now the optimal one, the filename's `<optimal_approach>`
  prefix may be wrong — **rename the file** accordingly and **update its row in the README
  index** to match.
- If the user has now written the optimal approach themselves, **remove any earlier
  `AI (Claude) SOLUTION` block** you had added — it's redundant now.

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

   **Actually analyze optimality — never assume it.** Read and understand the code
   before labeling anything. It is your responsibility to judge whether each approach
   is correct and whether it is truly optimal:
   - Verify correctness (trace the sample if one exists).
   - Work out the real time/space complexity.
   - Decide if a better approach exists. If the user's best solution is **not** optimal,
     say so explicitly in the comment — e.g. note that it could be done in O(n) with a
     hashmap, or in O(log n) with binary search — and briefly describe the better idea.
     The point of this archive is to help the user later, so an honest "this works but a
     faster approach is X" is more valuable than a rubber-stamped "OPTIMAL".
   - Only call an approach optimal when you have actually confirmed it. If the user has
     multiple approaches, mark which is genuinely best; if even the best is suboptimal,
     state what the optimal approach would be even if they didn't write it.

   **If the user's best solution is suboptimal, ADD the optimal approach in full.** Don't
   just describe it in prose — append a new block containing the actual optimal code
   (working Python, or clear pseudocode if a full impl is impractical), with its technique
   name and complexity, so the user can study and compare it later. This is additive (it
   never touches the user's own code — see rule 4).

   **Always place this added solution at the END of the file, and explicitly fence it as
   Claude's/AI's contribution with a clear marker at BOTH the top and the bottom**, so it's
   unmistakable which code is the user's and which was added by the AI:

   ```python
   # ===================== AI (Claude) SOLUTION — START =====================
   # Approach (OPTIMAL — added by Claude): Hash map  —  O(n) time, O(n) space
   # The user's solution above is O(n^2); this is the faster way to do it.
   # =======================================================================
   def ...

   # ====================== AI (Claude) SOLUTION — END ======================
   ```

   If the user's own solution is already optimal, no extra block is needed — just say so.

4. **Additive only — never delete or rewrite what the user already wrote.** The user's
   files usually contain scratch notes, worked examples, and random thought-process
   scribbles (often half-finished or commented out). These are kept on purpose — they
   help the user recall the problem later. Leave every existing line untouched. Your
   edits should only *add* things (the labeled approach headers, a tidied
   problem-statement block, a missing import). Do NOT rewrite the user's logic, refactor
   working code, or strip their notes unless explicitly asked. Keep edits minimal.

5. **Update the README index.** `README.md` has an `## Index` table
   (`Problem | Optimal approach | File`). Add one row for the new problem, with the File
   cell as a clickable relative link, e.g.
   `[dfs_course_schedule.py](problems/dfs_course_schedule.py)`. This is the user's
   clickable index of everything archived — keep it current on every new problem.

6. **Update `problem_context.md`.** Add (or update) the file's row in the context lookup
   table — `File | Context`, with a keyword-rich 2-3 line description of the problem's
   real-world subject, its input, the approaches used, and which is optimal. This is the
   table you consult to find a file from a vague description, so keep it current on every
   new problem AND whenever an existing file's approaches/optimal verdict change. If a
   file is renamed, update its path here too.

7. **Report, don't push.** Tell the user the final filename and show how the file
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
- Root holds only `README.md`, `CLAUDE.md`, `problem_context.md`, `.gitignore`.

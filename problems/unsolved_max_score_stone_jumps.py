# Problem: Maximum Score Stone Jumps
# Status: UNSOLVED (question only — to solve later)
#
# You are given a sequence of stones, each represented by a non-negative integer. Your task is to calculate the maximum possible score by jumping from the beginning of the sequence to the end.

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



# dp - O(n)





# dp[i] -> what is the max score possible to reach ith stone 

        


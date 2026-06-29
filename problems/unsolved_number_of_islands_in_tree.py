# Problem: Number of Islands in a Tree  (Google phone screen)
# Status: UNSOLVED (question only — to solve later)
# Source: https://leetcode.com/discuss/post/1682632/google-phone-screen-number-of-islands-in-zsmr/

# Google | Phone Screen | Number of Islands in a Tree

# Anonymous User
# 7579
# Jan 11, 2022
# Jan 11, 2022
# Google
# Phone Screening
# Interview
# Company: Google
# Stage: Phone Screen

# Given a tree having nodes with value 0 and 1. write a function to return the number of islands ?

# Follow Up Questions: (Asked by me)

# Are we giving root node as start node or it can vary ?
# Maximum number of children nodes for the node ?
# My Approach:

# Defined the custom node as follows:

# class TreeNode{
    
#     int value;
    
#     List<TreeNode> nextNodes;
   
#     // Constructor
#     TreeNode(int value){
#       this.value = value;
#       this.nextNodes = new LinkedList<>();
#     }
#   }
# Given DFS Approach by maintaining the Visited Set of nodes.

# Interviewer expected the O(n) Time complexity and O(1) Space Complexity

# I am unable to find the question in leetcode. Can anyone please suggest me better appraoch here ?


# Let's take the following tree as an example. We can see that it has 4 islands of 1's.

#     0
#   / | \
# 0   1  1
# |   |  |
# 1   0  1
#     |  
#     1   



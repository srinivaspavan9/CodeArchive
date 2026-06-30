# Problem: Number of Islands in a Tree  (Google phone screen)
# Status: SOLVED
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


# Assumpitons
# A node can have how ever many childre it can 
# The root node will be given for traversal

class Node:
	def __init__(self,val):
		self.val=val
		self.nextNodes=[]


# ============================================================
# Approach 1: DFS flood-fill (mark each island)  —  intended O(n) time
# ============================================================
# Walk the tree; on a 1-node, flood-fill its connected group of 1s and add 1.
# Two bugs as written (kept as-is; noted so you can fix on revision):
#   1) `cnt += 1` in the nested dfs() needs `nonlocal cnt`, else UnboundLocalError.
#   2) mark() sets node.val = 1 (no-op) instead of sinking visited 1s to 0, so the
#      later dfs() re-walks island interiors and overcounts (sample => 5, not 4).
#      Fix: have mark() set node.val = 0.

# Brute Force Approach

def countIslandsInATree(root):
	cnt=0

	def dfs(root):
		def mark(node):
			node.val=1
			for nextNode in node.nextNodes:
				if nextNode.val==1:
					mark(nextNode)

		if not root:
			return
		for node in root.nextNodes:
			if node.val==1:
				mark(node)
				cnt+=1
			dfs(node)

	dfs(root)
	return cnt


# ============================================================
# Approach 2 (best here): Union-Find over the 1-nodes  —  O(n) time, O(n) space
# ============================================================
# Give each 1-node its own set, union it with its parent when the parent is also
# 1; islands = number of distinct set roots. Logic is correct. Two notes:
#   1) Won't run as written — the union()/dfs() bodies mix spaces with the tabs
#      used elsewhere => TabError. Re-indent consistently (all tabs or all spaces).
#   2) Uses an O(n) parent map => O(n) space, above the interviewer's O(1) target
#      (the O(1)-space way: count nodes where val==1 and parent's val != 1).

# Using Disjoint Sets ( Union - Find) and DFS or BFS

def countIslandsInATree(root):
	parent={}

	def find(x):
		if parent[x]!=x:
			parent[x]=find(parent[x])
		return parent[x]

	def union(a,b):
		ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    def dfs(par,node):
    	if not node:
    		return

    	if node.val==1:
    		parent[node]=node
    		if par is not None and par.val==1:
    			union(node,par)

    	for child in node.nextNodes:
    		dfs(child,node)

    dfs(root,None)
    cnt = 0
    for node in parent:
    	if parent[node]==node:
    		cnt+=1
    return cnt
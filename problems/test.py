# Problem Description
# In a chess tournament with N players, each player has a distinct rank from 1 to N 
# (where rank 1 is the best player and rank N is the worst). In any game between two players, 
# the higher-ranked player (lower rank number) always wins.

# Given the results of M games in the format [winner, loser], determine which players' ranks can be precisely determined.

# A player's rank can be precisely determined if we can establish their exact position in the ranking through the transitive 
# relationships from all game results.

# Function Signature
# vector<pair<int, int>> determineRanks(vector<vector<int>>& games, int n);
# Parameters:

# games: A 2D array where games[i] = [winner, loser] represents that player winner beat player loser
# n: The total number of players (numbered from 1 to n)
# Returns:

# A vector of pairs [player, rank] for players whose ranks can be precisely determined


Sample Case
# Input: games = [[4,3],[4,2],[3,2],[1,2],[2,5]], n = 5
# Output: [[2,4],[5,5]]


# [4, 3], [3, 2], [2, 5], [4,2] , [1,2]

# Explanation:
# - Player 2 lost to players 1, 3, 4 and won against player 5
# - Since we know 3 players beat player 2 and player 2 beats 1 player, 
#   player 2's rank is precisely 4 (3 + 1 = 4)
# - Player 5 lost to player 2, and we know player 2 lost to 3 other players
# - So player 5 is beaten by all other players, making their rank precisely 5

given n players there should be n ranks 

# 4, 3 

# loss 3 - 1
# 4, 2 
# loss 2 - 1
# 3, 2

# loss 2 -2+loss(3)




# 1st rank - loses to 0 person
# 2nd rank - loses to 1 person
# kth rank - loses to k-1 persons
# loss(5) = currloss(5)+loss(2) 1+loss(2)
# rank(5) = loss(5)+1


# [4, 3], [3, 2], [2, 5], [4,2] , [1,2]

# [[1, 2], [2, 3]]
    a  b



# def countlosses(a,b,loss):
#     # if loss[b]!=-1 return loss[b]
#     loss[b]=1+loss[b]+countlosses(a)
#     # return loss[b]

# def countWins(a,b,wins):
#     # if wins[a]!=-1 return wins[a]
#     wins[a]=1+wins[a]+countWins(b)
#     # return wins[a]

# loss(3) - 1
# win( 4) - 1

# win(3) - 1+win(2) -1
# loss(2) - 1+loss(3)- 2

# win(2) - 1+ win(5)- 1
# loss(5) 1+ loss(2) 1+2 -> 3

# wins(4) -> curwins(4)+wins(2) -> 1+1 = 2
# loss(2) -> 1+2+loss(4) -> 3

# wins(1) - > 1+curwins(1)+wins(2) ->




def countPlayers(player, graph, visited):
    count = 0
    for oppnt in graph[player]:
        if oppnt not in visited:
            visited.add(oppnt)
            count = count + 1 + countPlayers(oppnt, graph, visited)
    return count                                   

def determineRanks(games, n):
    winGraph = defaultdict(list)
    lossGraph = defaultdict(list)
    for game in games:
        winGraph[game[0]].append(game[1])
        lossGraph[game[1]].append(game[0])
    ranks = []
    for player in range(1, n + 1):
        visited = set()
        wins = countPlayers(player, winGraph, visited)     
        visited = set()
        loss = countPlayers(player, lossGraph, visited)     
        if wins + loss == n - 1:
            ranks.append([player, loss + 1])
    return ranks
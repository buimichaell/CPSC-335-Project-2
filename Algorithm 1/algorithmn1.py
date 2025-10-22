# Project 2
# Algorithm 1 - Movement of Knights
# ===================================
# Member Names:
# - Michael Bui
# - Natalia Garcia
# ===================================
# *** Psedocode ***
# FUNCTION knight_distance(a_row, a_col, b_row, b_col):
#   IF (a_row, a_col) = (b_row, b_col) RETURN 0
#   moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
#   q = [(a_row, a_col, 0)]; seen = {(a_row, a_col)}
#   M = max(|a_row|,|a_col|,|b_row|,|b_col|) + 6; lo = -M; hi = M
#   WHILE q not empty:
#       (row, col, dist) = pop_front(q)
#       FOR (dr, dc) IN moves:
#           new_row = row + dr; new_col = col + dc
#           IF (new_row, new_col) = (b_row, b_col) RETURN dist + 1
#           IF lo≤new_row≤hi AND lo≤new_col≤hi AND (new_row,new_col) NOT IN seen:
#               add (new_row,new_col) to seen; push_back(q,(new_row,new_col,dist+1))
#   RETURN -1
# FUNCTION min_turns(knightA, knightB):
#   d = knight_distance(knightA[0],knightA[1],knightB[0],knightB[1])
#   RETURN (d+1) // 2
# A=[0,0]; B=[4,2]
# ans = min_turns(A,B)
# PRINT ans
# WRITE ans+"\n" TO "output.txt"
# ====================================== 

from collections import deque
import math

def knight_distance(ax, ay, bx, by): #Finds the minimum number of knight moves between the squares
    if ax == bx and ay == by:
        return 0 #Returns if already on the same square.

    #All the L moves a knight can make.
    moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    #BFS setup
    q = deque()
    q.append((ax, ay, 0))
    seen = set([(ax, ay)]) #Avoids knights from revisting squares.

    #Soft boundary
    M = max(abs(ax), abs(ay), abs(bx), abs(by)) + 6
    lo, hi = -M, M

    #Implemented BFS over the board squares.
    while q:
        x, y, d = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (bx, by):
                return d + 1 #returns if the target square is met
            if lo <= nx <= hi and lo <= ny <= hi and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((nx, ny, d + 1))
    return -1

def min_turns(knightA, knightB):
    d = knight_distance(knightA[0], knightA[1], knightB[0], knightB[1])
    #Each turn allows for two half moves
    return (d + 1) // 2  if d % 2 == 1 else d // 2

#output testing
knightA = [0, 0]
knightB = [4, 2]
print(min_turns(knightA, knightB)) #output should expect 1

ans = min_turns(knightA, knightB)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(ans) + "\n")

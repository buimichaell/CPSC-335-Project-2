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

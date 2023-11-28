import sys
sys.setrecursionlimit(10**5)
import collections

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    answer = []
    
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != "X" and not visited[i][j]:
                land = 0
                q = collections.deque([(i, j)])
                
                while q:
                    x, y = q.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    land += int(maps[x][y])
                    
                    for direction in range(4):
                        new_x, new_y = x + dx[direction], y + dy[direction]
                        if (0 <= new_x < rows and 0 <= new_y < cols and
                            maps[new_x][new_y] != "X" and not visited[new_x][new_y]):
                            q.append((new_x, new_y))
                
                answer.append(land)

    return sorted(answer) if answer else [-1]

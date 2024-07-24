import sys
sys.setrecursionlimit(10**6)

n = int(input())
frame = []
for i in range(n):
    frame.append(list(input()))

normal_visited = [[0]*n for _ in range(n)]
abnormal_visited = [[0]*n for _ in range(n)]

def dfs(x, y, color, visited):
    if 0 <= x < n and 0 <= y < n and not visited[x][y] and frame[x][y] == color:
        visited[x][y] = 1
        dfs(x-1, y, color, visited)
        dfs(x+1, y, color, visited)
        dfs(x, y-1, color, visited)
        dfs(x, y+1, color, visited)
        return 1
    return 0

normal, abnormal = 0, 0
normalRgb, abnormalRgb = ['R', 'G', 'B'], ['R', 'B']

for color in normalRgb:
    for i in range(n):
        for j in range(n):
            normal += dfs(i, j, color, normal_visited)

for i in range(n):
    for j in range(n):
        if frame[i][j] == 'G':
            frame[i][j] = 'R'

for color in abnormalRgb:
    for i in range(n):
        for j in range(n):
            abnormal += dfs(i, j, color, abnormal_visited)

print(normal, abnormal)

from collections import deque
n = int(input())
frame = []
for i in range(n):
    frame.append(list(input()))
    
def bfs(frame, color):
    result = 0 
    q = deque()
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[0] * len(frame) for _ in range(len(frame))]
    
    for i in range(len(frame)):
        for j in range(len(frame)):
            if frame[i][j] == color and not visited[i][j]:
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx,ny = x+direction[k][0], y+direction[k][1]
                        if 0<=nx<len(frame) and 0<=ny<len(frame) and frame[nx][ny] == color and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                result += 1
    return result

normal, abnormal = 0,0
normalRgb = ['R','G','B']
abRgb = ['R','B']

for color in normalRgb:
    normal += bfs(frame,color)

for i in range(n):
    for j in range(n):
        if frame[i][j] == 'G':
            frame[i][j] = 'R'

for color in abRgb:
    abnormal += bfs(frame,color)

print(normal, end =' ')
print(abnormal)
    

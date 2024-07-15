from collections import deque

m,n = map(int,input().split())
box = []
answer = 0
direction = [[-1,0], [1,0], [0,1],[0,-1]]

for i in range(n):
    box.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i,j,0))

while q:
    x,y,day = q.popleft()
    for i in range(4):
        nx, ny = x+direction[i][0], y+direction[i][1]
        if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
            box[nx][ny] = 1
            q.append((nx,ny,day+1))
            answer = day + 1
    
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            answer = -1

print(answer)

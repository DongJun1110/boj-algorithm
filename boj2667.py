from collections import deque

n = int(input())
houses = []
frame = []
direction = [[-1,0],[1,0],[0,-1],[0,1]]
for i in range(n):
    frame.append(list(map(int,input())))
      
def bfs(x,y):
    q = deque()
    cnt = 1
    frame[x][y] = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+direction[i][0], y+direction[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if frame[nx][ny] == 0:
                continue
            q.append((nx,ny))
            frame[nx][ny] = 0
            cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if frame[i][j] == 1:
            houses.append(bfs(i,j))

print(len(houses))
houses.sort()
for house in houses:
    print(house)

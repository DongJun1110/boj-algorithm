from collections import deque

n,m = map(int,input().split())
frame = [] 
for _ in range(n):
    frame.append(list(map(int,input())))

direction = [[-1,0],[1,0],[0,-1],[0,1]]
q = deque()
q.append((0,0))

while q:
    x,y = q.popleft()
    for i in range(4):
        dx, dy = x+direction[i][0], y+direction[i][1]
        if dx<0 or dy<0 or dx>=n or dy>=m:
            continue
        if frame[dx][dy] == 0:
            continue
        if frame[dx][dy] == 1:
            q.append((dx,dy))
            frame[dx][dy] = frame[x][y]+1

print(frame[n-1][m-1])


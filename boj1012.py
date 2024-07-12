from collections import deque
T = int(input())
direction = [[-1,0],[1,0],[0,-1],[0,1]]
for tc in range(T):
    m,n,k = map(int,input().split())
    answer = 0
    q = deque()
    field = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                answer += 1
                field[i][j] = 0
                q.append((i,j)) 
                while q:
                    x,y = q.popleft()
                    for l in range(4):
                        nx, ny = x+direction[l][0], y+direction[l][1]
                        if 0<=nx<n and 0<=ny<m and field[nx][ny] == 1:
                            q.append((nx,ny))
                            field[nx][ny] = 0
    print(answer)

        

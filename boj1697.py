from collections import deque
n,k = map(int,input().split())
visited = [0]*1000000
q = deque()
q.append((n,0))
visited[n] = 1
while q:
    pos, sec = q.popleft()
    if pos == k:
        print(sec)
        break
    for next_pos in [pos-1, pos+1, pos*2]:
        if not visited[next_pos] and 0<=next_pos<100001:
            q.append((next_pos,sec+1))
            visited[next_pos] = 1

from collections import deque

def virus(web):
    contracted = [1]
    q = deque()
    q.append(1)
    while q:
        next = q.popleft()
        victims = web[next]
        for victim in victims:
            if victim in contracted:
                continue
            q.append(victim)
            contracted.append(victim)
    return len(contracted)

com = int(input())
conn = int(input())
frame = [[] for i in range(com+1)]
result = 0
for i in range(conn):
    x,y = map(int,input().split())
    frame[x].append(y)
    frame[y].append(x)
    
print(virus(frame)-1)
    

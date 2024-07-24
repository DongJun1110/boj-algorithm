from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for edges in graph:
    edges.sort()
    
def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    print(start, end = ' ')
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                print(i,end=' ')
                
def dfs(graph, start, visited):
    visited[start] = 1
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
dfs_visited = [0]*(n+1)
bfs_visited = [0]*(n+1)

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)


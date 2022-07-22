from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

dfs_list = []
bfs_list = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx, g in enumerate(graph):
    g.sort()
    
def dfs(graph, v, visited, list_dfs):
    visited[v] = True
    list_dfs.append(v)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, list_dfs)
            
def bfs(graph, start, visited, list_bfs):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        list_bfs.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, V, visited_dfs, dfs_list)
bfs(graph, V, visited_bfs, bfs_list)

print(*dfs_list)
print(*bfs_list)
    
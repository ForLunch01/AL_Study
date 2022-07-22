import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

edge_list = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    edge_list[a].append(b)
    edge_list[b].append(a)

for e in edge_list:
    e.sort()
    
visited = [False] * (N+1)
visited_list = []

def dfs(visited, v, graph, dfs_list):
    visited[v] = True
    dfs_list.append(v)
    
    for g in graph[v]:
        if not visited[g]:
            dfs(visited, g, graph, dfs_list)
            
dfs(visited, 1, edge_list, visited_list)

print(len(visited_list)-1)
    
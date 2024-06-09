import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
	p, c, w = map(int, input().split(' '))
	graph[p].append([c, w])
	graph[c].append([p, w])

# print(graph)

def dfs(start, w_cur):
	for st in graph[start]:
		node_nxt, w_nxt = st
		if dist[node_nxt] == -1:
			dist[node_nxt] = w_cur + w_nxt
			dfs(node_nxt, w_cur + w_nxt)

dist = [-1 for _ in range(n+1)]
dist[1] = 0
dfs(1, 0)


start = dist.index(max(dist))
dist = [-1 for _ in range(n+1)]
dist[start] = 0
dfs(start, 0)
print(max(dist))

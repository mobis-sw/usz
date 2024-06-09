import sys
sys.stdin = open("input.txt",'r')

from collections import deque


n, m, t = map(int, input().split(' '))

arr = [list(map(int, input().split(' '))) for _ in range(n)]
# print(arr)
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

q = deque()

q.append([0, 0])

flag = 0
answer = 0

def bfs(q):
	ret = 10001
	while q:
		r, c = q.popleft()
		
		if (r == (n-1)) and (c == (m-1)):
			ret = min(ret, visited[r][c]-1)
			return ret
	
		for d in range(4):
			nr, nc = r + dr[d], c + dc[d]
			if -1 < nr < n and -1 < nc < m:
				if visited[nr][nc] == 0:
					if arr[nr][nc] == 0:
						visited[nr][nc] = visited[r][c] + 1
						q.append([nr, nc])

					if arr[nr][nc] == 2:
						visited[nr][nc] = visited[r][c] + 1
						ret = min(ret, visited[nr][nc] + abs(n - 1 - nr) + abs(m - 1 - nc) - 1)
	return ret

answer = bfs(q)

# print(visited)

print('Fail' if answer > t else answer)

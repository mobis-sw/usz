from collections import deque

def bfs():
	# print(pos)
	q = deque()
	q.append([pos[0][0], pos[0][1]])
	while q:
		x, y = q.popleft()
		# print(x, y)
		if abs(x - pos[-1][0]) + abs(y - pos[-1][1]) <= 1000:
			print("happy")
			return

		for i in range(1, n+1):
			nx, ny = pos[i][0], pos[i][1]
			if abs(x - nx) + abs(y - ny) <= 1000:
				if not visited[i-1]:
					visited[i-1] = 1
					q.append([nx, ny])

		# print(q)
	print("sad")


t = int(input())

for _ in range(t):
	n = int(input())
	pos = []
	visited = [0 for _ in range(n)]
	for _ in range(n+2):
		pos.append(list(map(int, input().split())))

	bfs()

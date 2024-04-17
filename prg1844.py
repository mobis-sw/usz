#1844

from collections import deque
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    
    def bfs(q):
        while q:
            r, c = q.popleft()
            if r == (n-1) and c == (m-1):
                break
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if -1 < nr < n and -1 < nc < m:
                    if maps[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append([nr, nc])

#     def dfs(r, c):
#         if r == (n-1) and c == (m-1):
#             return
        
#         for d in range(4):
#             nr, nc = r + dr[d], c + dc[d]
#             if -1 < nr < n and -1 < nc < m:
#                 if maps[nr][nc] == 1 and visited[nr][nc] == 0:
#                     visited[nr][nc] = visited[r][c] + 1
#                     dfs(nr, nc)
    
    # main
    q = deque([[0, 0]])
    bfs(q)
    if visited[n-1][m-1] == 0: cnt = -1
    else: cnt = visited[n-1][m-1]
    answer = cnt
    # print(visited)
    
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/154540


from collections import deque

def solution(maps):
    answer = []
    # B-F OK
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]
    q = deque()
    area = list()
    sum_area = 0
    def bfs(q):
        nonlocal area, sum_area
        while q:
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if -1 < nr < n and -1 < nc < m and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = 1
                    sum_area += int(maps[nr][nc])
                    q.append([nr, nc])
        area.append(sum_area)
        
    
    # main
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                sum_area = int(maps[i][j])
                visited[i][j] = 1
                q.append([i, j])
                bfs(q)
    
    
    if len(area) == 0: answer = [-1]
    else:
        area.sort()
        answer = area
        
    return answer

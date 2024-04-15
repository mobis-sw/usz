#43162

def solution(n, computers):
    # 1<= n <= 200; O(N^2)
    # computers; adjacency matrix
    answer = 0
    visited = [0] * n
    
    def dfs(cur):
        nonlocal computers, visited
        for v in range(len(computers)):
            if visited[v] == 0 and computers[cur][v] == 1:
                visited[cur] = 1
                dfs(v)
    
    # main
    while False in visited:
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                answer += 1
            
    return answer

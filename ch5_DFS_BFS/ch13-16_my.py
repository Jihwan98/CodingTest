# ch13-16 연구소
from itertools import combinations
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph1 = graph.copy()

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph1[x][y] != 2:
        return False
    if graph1[x][y] == 2:
        graph1[x][y] == 3
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph1[nx][ny] == 0:
                graph1[nx][ny] = 2
            dfs(nx, ny)
        return True
    return False

air_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            air_list.append((i, j))

block_combinations = list(combinations(air_list, 3))

result = 0
for place in block_combinations:
    now_result = 0 
    graph1 = graph.copy()
    for x, y in place:
        graph1[x][y] = 1
    for i in range(n):
        for j in range(m):
            dfs(i, j)
    
    for i in range(n):
        for j in range(m):
            if graph1[i][j] == 0:
                now_result += 1
    result = min(result, now_result)

print(result)
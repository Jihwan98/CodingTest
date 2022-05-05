# 뱀
from collections import deque

n = int(input())
way_map = [[0]*n for _ in range(n)]
apple = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
  row, col = map(int, input().split())
  apple[row-1][col-1] = 1 # 사과

l = int(input())
data = deque()
for _ in range(l):
  data.append(input().split())
data.append([-1, -1]) # data를 모두 실행 되었을 때 대비
x, y = 0, 0 # x : row, y : col
way_map[x][y] = 1
way = deque()
way.append((x,y))
direction = 0 # 0 : 우, 1 : 하, 2 : 좌, 3 : 상
dir_option = {'D':1, 'L':-1}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
length = 1
while True:
  time += 1
  nx = x + dx[direction]
  ny = y + dy[direction]
  if nx < 0 or nx >= n or ny < 0 or ny >= n:
    break
  way_map[nx][ny] += 1
  if way_map[nx][ny] >= 2:
    break
  way.append((nx, ny))
  if apple[nx][ny] != 1:
    way_map[way[0][0]][way[0][1]] -= 1
    way.popleft()
  
  if int(data[0][0]) == time:
    direction = (direction + dir_option[data[0][1]]) % 4
    data.popleft()

  x, y = nx, ny

print(time)
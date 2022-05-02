# 게임 개발
n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []
for i in range(n):
    line = list(map(int, input().split()))
    game_map.append(line)
game_map[x][y] = 2

dx = [-1, 0, 1, 0] # row
dy = [0, 1, 0, -1] # column

result = 0
turn_count = 0

while True:
    d = (d - 1) % 4

    nx = x + dx[d]
    ny = y + dy[d]

    if game_map[nx][ny] == 0:
        x, y = nx, ny
        game_map[nx][ny] = 2
        result += 1
        turn_count = 0
    else:
        turn_count += 1
        if turn_count == 4:
            nx = x + dx[(d+2) % 4]
            ny = y + dy[(d+2) % 4]
            
            if game_map[nx][ny] == 1:
                break
            x, y = nx, ny
            turn_count = 0

print(result)
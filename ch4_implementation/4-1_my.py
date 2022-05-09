# 상하좌우
n = int(input())
data = list(input().split())

place = [1, 1]

for d in data:
  if d == 'L':
    if place[1] == 1:
      continue
    place[1] -= 1
  elif d == 'R':
    if place[1] == n:
      continue
    place[1] += 1
  elif d == 'U':
    if place[0] == 1:
      continue
    place[0] -= 1
  elif d == 'D':
    if place[0] == n:
      continue
    place[0] += 1

print(place[0], place[1])
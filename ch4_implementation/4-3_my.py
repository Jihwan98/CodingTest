# 왕실의 나이트

pos = input()

x = int(pos[1])
y = ord(pos[0]) - ord('a') + 1

d1 = [1, -1, 2, -2]

count = 0
for i in range(4):
    nx = x + d1[i]
    for j in range(2):
        if i < 2:
            ny = y + d1[j+2]
        else:
            ny = y + d1[j]
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        count += 1

print(count)
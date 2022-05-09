n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

count = 0
sum = 0
for i in range(m):
    if count == k:
        sum += data[1]
        count = 0
        continue
    sum += data[0]
    count += 1

print(sum)

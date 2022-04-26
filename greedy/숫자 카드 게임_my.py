n, m = map(int, input().split())
data = list()
for i in range(n):
    d = list(map(int, input().split()))
    data.append(d)

result = 0
for i in data:
    i.sort()
    if i[0] > result:
        result = i[0]

print(result)
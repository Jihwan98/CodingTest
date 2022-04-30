# 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
count = 0
for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[i] != data[j+1+i]:
            count += 1
print(count)
# 모험가 길드
n = int(input())
data = list(map(int, input().split()))
result = 0
data.sort()
count = 0
for i in data:
  count += 1 # 그룹에 포함된 모험가 수
  if count >= i:
    result += 1
    count = 0
print(result)
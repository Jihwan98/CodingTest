# 모험가 길드
n = int(input())
data = list(map(int, input().split()))
result = 0
data.sort(reverse=True)

while True:
  if not data:
    break
  max_data = data[0]
  if n < max_data or n == 0:
    break
  n -= max_data
  result += 1
  data = data[max_data:]

print(result)
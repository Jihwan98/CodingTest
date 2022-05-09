# 문자열 뒤집기
import math
data = input()

last = data[0]
result = 0
for i in data:
  if last != i:
    result += 1
  last = i

result = math.ceil(result / 2)
print(result)
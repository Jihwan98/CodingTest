# 곱하기 혹은 더하기

s = input()

result = int(s[0])

if result == 0:
  mul = False
else:
  mul = True
for i in s[1:]:
  if mul:
    result *= int(i)
  else:
    result += int(i)
  if int(i) <= 1:
    mul = False
  else:
    mul = True
  
print(result)


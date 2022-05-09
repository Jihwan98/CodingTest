# 럭키 스트레이트

n = input()

half = len(n) / 2

left = 0
right = 0
for i in range(int(half)):
    left += int(n[i])
    right += int(n[int(half)+i])

if left == right:
    print("LUCKY")
else:
    print("READY")
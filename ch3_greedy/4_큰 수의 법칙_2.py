# m 이 100억 이상처럼 커지면 시간 초과 판정을 받을 것
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

# (k + 1)의 수열으로 반복되는 것을 이용

first = data[0]
second = data[1]
result = (m // (k+1)) * (first*k + second) + (m % (k+1)) * first
print(result)

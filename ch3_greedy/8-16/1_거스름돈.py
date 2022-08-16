n = int(input())
coins = [500, 100, 50, 10]
result = 0
for c in coins:
    result += n // c
    n = n % c

print(result)
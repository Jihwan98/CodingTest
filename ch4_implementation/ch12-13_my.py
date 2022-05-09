# 치킨 배달
from itertools import combinations
n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

chicken = 0
for i in city:
    for j in i:
        if j == 2:
            chicken += 1
del_num = chicken - m

def calculate_time(city):
    time = 0
    for r in range(n):
        for c in range(n):
            if city[r][c] == 1:
                short_time = 2*n
                for i in range(n):
                    for j in range(n):
                        if city[i][j] == 2:
                            temp_time = abs(r-i) + abs(c-j)
                            if temp_time < short_time:
                                short_time = temp_time
                time += short_time

    return time

chicken_r_c = []
for r in range(n):
    for c in range(n):
        if city[r][c] == 2:
            chicken_r_c.append((r, c))

if del_num > 0:
    chicken_combination = list(combinations(chicken_r_c, del_num))
    answer = 999999999

    for places in chicken_combination:
        city_ = city.copy()
        for r, c in places:
            city_[r][c] = 0
        
        time = calculate_time(city_)
        if time < answer:
            answer = time
else:
    answer = calculate_time(city)
print(answer)
# 무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    time = 0
    for i in range(k):
        if food_times[time%(len(food_times))] == 0:
            time += 1
        food_times[time%(len(food_times))] -= 1
        time += 1
    if sum(food_times) == 0:
        answer = -1
    else:
        answer = time % len(food_times) + 1
    
    return answer

    # 틀렸음
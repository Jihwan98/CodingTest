# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        elif operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)
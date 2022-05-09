# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    wall_0 = [[0]*(n+1) for _ in range(n+1)]
    wall_1 = [[0]*(n+1) for _ in range(n+1)]
    answer = []
    for x, y, a, b in build_frame: # x, y : 좌표, a : 구조물 종류(0은 기둥, 1은 보), b : 삭제(0) or 설치(1)
        if b == 1:
            possible = False
            if a == 0:
                if wall_1[n-y][x-1] == 1 or wall_1[n-y][x] == 1 or y == 0 or wall_0[n-(y-1)][x] == 1:
                    possible = True
            else:
                if wall_0[n-(y-1)][x] == 1 or wall_0[n-(y-1)][x+1] == 1 or (wall_1[n-y][x-1] == 1 and wall_1[n-y][x+1] == 1):
                    possible = True
            if possible:
                answer.append((x,y,a))
                if a == 0:
                    wall_0[n-y][x] = 1
                else:
                    wall_1[n-y][x] = 1
        else:
            answer.remove((x,y,a))
            if a == 0:
                wall_0[n-y][x] = 0
            else:
                wall_1[n-y][x] = 0
            for x_, y_, a_ in answer:
                possible = True
                if a_ == 0:
                    if not (wall_1[n-y_][x_-1] == 1 or wall_1[n-y_][x_] == 1 or y_ == 0 or wall_0[n-(y_-1)][x_] == 1):
                        possible = False
                        break
                else:
                    if not (wall_0[n-(y_-1)][x_] == 1 or wall_0[n-(y_-1)][x_+1] == 1 or (wall_1[n-y_][x_-1] == 1 and wall_1[n-y_][x_+1] == 1)):
                        possible = False
                        break
            if not possible:
                answer.append((x,y,a))
                if a == 0:
                    wall_0[n-y][x] = 1
                else:
                    wall_1[n-y][x] = 1
        
                
    answer.sort()
    return answer
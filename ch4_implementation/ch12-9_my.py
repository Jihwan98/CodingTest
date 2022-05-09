# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057 
def solution(s):
    length = len(s)
    min = length
    for i in range(1, (length//2 + 1)):
        result = []
        count = 1
        for j in range(0, length, i):
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count > 1:
                    result.append(str(count) + s[j:j+i])
                else:
                    result.append(s[j:j+i])
                count = 1
        if count > 1:
            result.append(str(count) + s[j:j+i])
        else:
            result.append(s[j+i:j+2*i])
        if (j+2*i) != length:
            result.append(s[j+2*i:])
        result_len = len(''.join(result))
        if result_len < min:
            min = result_len
        
    answer = min
    return answer
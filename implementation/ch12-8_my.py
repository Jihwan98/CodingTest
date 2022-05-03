# 문자열 재정렬
s = list(input())
s = sorted(s)

num_list = list('0123456789')
index, sum = 0, 0
for i in s:
    if i not in num_list:
        break
    index += 1
    sum += int(i)

str = ''
for i in s[index:]:
    str += i
print(f"{str}{sum}")
# 2차원 리스트 90도 회전
def rotate_matrix(matrix):
    n = len(matrix) # 행 길이
    m = len(matrix[0]) # 열 길이
    result = [[0]*n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = matrix[i][j]
    return result
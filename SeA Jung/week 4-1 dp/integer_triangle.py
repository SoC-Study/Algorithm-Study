"""
꼭대기 층부터 아래로 내려가면서 
각 위치 별로 가능한 최대의 수 구하기
"""


def solution(triangle):
    sum_triangle = triangle[:]
    depth = len(triangle)
    for i in range(depth):
        if i == 0:
            continue
        else:
            for j in range(i+1):
                if j == 0:
                    sum_triangle[i][j] = sum_triangle[i-1][j] + triangle[i][j]
                elif j == i:
                    sum_triangle[i][j] = sum_triangle[i -
                                                      1][j-1] + triangle[i][j]
                else:
                    sum_triangle[i][j] = max(
                        sum_triangle[i-1][j-1], sum_triangle[i-1][j]) + triangle[i][j]

    answer = max(sum_triangle[-1])
    return answer

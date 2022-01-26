'''
1. 전체 경우 - 물웅덩이를 지나는 경우의 수
물웅덩이를 두개 이상 지나는 경우 구하기 너무 귀찮을 것 같은데....
2. 각 꼭짓점마다 갈 수 있는 경로의 수 구하기

'''


def solution(m, n, puddles):

    #counts[n][m] = (m,n)
    counts = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                counts[i][j] = 0
            elif i == 1 and j == 1:
                counts[i][j] = 1
            else:
                counts[i][j] = counts[i][j-1] + counts[i-1][j]

    return counts[n][m] % 1000000007

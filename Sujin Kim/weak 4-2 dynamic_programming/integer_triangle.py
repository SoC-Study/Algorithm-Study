def solution(triangle):
    answer = 0
    depth = len(triangle)-1
    answer = triangle.copy()
    i = depth-1
    while(i>=0):
        j = 0
        while(j<=i):
            answer[i][j] = triangle[i][j] + max(answer[i+1][j], answer[i+1][j+1])
            j += 1
        i = i-1
    return answer[0][0]

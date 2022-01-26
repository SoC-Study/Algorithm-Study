def find_max(triangle,i, L, depth):
    if(L==depth):
        return triangle[L][i]        
    return triangle[L][i] + max(find_max(triangle, i, L+1, depth), find_max(triangle, i+1, L+1, depth))

def solution(triangle):
    answer = 0
    depth = len(triangle)-1
    i = 0
    L = 0
    return find_max(triangle,i, L, depth)

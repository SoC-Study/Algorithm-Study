def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    
    while((scoville[0] < K) and (len(scoville))>1):
        first = scoville.pop(0)
        second = scoville.pop(0)
        scoville.append(first + second*2)
        answer = answer + 1
        scoville.sort()
        
    if(scoville[0] >= K):
        return answer
    return -1

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) < 2:
            return -1
        min_sco1 = heapq.heappop(scoville)
        min_sco2 = heapq.heappop(scoville)
        mixed_sco = min_sco1 + min_sco2*2
        heapq.heappush(scoville, mixed_sco)
        answer += 1
        if scoville[0] >= K:
            break
            
    return answer

# testcase
scoville = [1, 2, 3, 9, 10, 12]	
K = 7
print(solution(scoville, K))    # 2
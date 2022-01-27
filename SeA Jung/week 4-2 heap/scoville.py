"""
1. sorting을 통해서 가장 작은것 끼리 더해간다
-> 효율성 테스트에서 타임아웃
2. 힙을 만들어서 자식들을 더해가며 힙을 수정해나간다.

"""

""" 
# 1. sorting을 통해서
def solution(scoville, K):
    answer = 0
    while len(scoville) >1 and min(scoville) < K :
        scoville.sort()
        min1 = scoville[0]
        min2 = scoville[1]
        
        mixed = min1 + min2*2
        scoville = scoville[2:] + [mixed]
        answer +=1
    
    if scoville[0] <K:
        return -1
    return answer
"""

# 2. heap을 통해서




import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)

    while len(heap) > 1:

        min1 = heapq.heappop(heap)
        if min1 > K:
            break
        min2 = heapq.heappop(heap)
        mixed = min1 + min2*2
        heapq.heappush(heap, mixed)
        answer += 1

    if heap[0] < K:
        return -1
    return answer

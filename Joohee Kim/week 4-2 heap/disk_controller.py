'''
요청시점이 현재보다 전이면, ready_heap 에 넣기 (시간 지남에 따라 게속 업데이트)
ready_heap에 있는 작업 중 소요시간 가장 작은 것부터 처리
'''

import heapq

def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x: (x[0], x[1])) # 작업요청시간 기준 정렬

    j = jobs.pop(0)
    ready_heap = [[j[1], j[0]]]
    curr_time = j[0]
    
    for start, time in jobs:
        while ready_heap and start >= curr_time:   
            curr_t, curr_s = heapq.heappop(ready_heap)
            answer = answer + (curr_time + curr_t - curr_s)
            curr_time += curr_t
            
        # 요청시점이 현재시간보다 전 --> ready_heap에 삽입
        if start < curr_time:
            heapq.heappush(ready_heap, [time, start])
        else:   # 중간에 공백이 있는 경우(readyheap is empty) --> 강제로 처리
            answer =  answer + time
            curr_time = start + time
        
    while ready_heap:
        curr_t, curr_s = heapq.heappop(ready_heap)
        answer = answer + (curr_time + curr_t - curr_s)
        curr_time += curr_t
        
    answer = answer // len(jobs)
    
    return answer
# testcase
jobs = [[0, 3], [1, 9], [2, 6]]
jobs2 = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]   #72
jobs3 = [[0, 5], [2, 10], [100, 2]] #6
print(solution(jobs3))
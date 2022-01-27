"""
현재 시간 이전에 들어온 요청을 힙에 담는다.
진행 시간이 가장 짧은 순으로 진행 -> clock update
"""
import heapq


def solution(jobs):
    answer = 0
    clock, jobs_done = 0, 0

    heap = []
    num_jobs = len(jobs)
    jobs.sort()
    while jobs_done < num_jobs:
        while jobs:
            if jobs[0][0] <= clock:
                heapq.heappush(heap, (jobs[0][1], jobs[0][0]))
                jobs.pop(0)
            else:
                break

        if heap:
            curr_job = heapq.heappop(heap)
            clock += curr_job[0]
            answer += clock - curr_job[1]
            jobs_done += 1
        else:
            clock += 1

    answer = answer // num_jobs

    return answer

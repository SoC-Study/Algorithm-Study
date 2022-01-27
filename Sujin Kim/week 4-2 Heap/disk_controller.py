def solution(jobs):
    answer = 0
    position = 0
    L = len(jobs)
    
    while(len(jobs)>0):
        
        minn = 1001 #min의 실행시간
        minn_idex = 501 #min의 인덱스
        minn_start = 501 #min의 작업 허용 위치
        
        for idx, ele in enumerate(jobs):
            if(ele[0]<=position): # 작업이 허용된 것만
                if(minn > ele[1]): 
                    minn_start = ele[0]
                    minn = ele[1]
                    minn_idex = idx
        if minn_idex == 501: # 작업에 허용된 것이 아무도 없을 때
            position += 1
        else:
            position = position + minn
            jobs.pop(minn_idex)
            answer = answer + (position-minn_start)
            
    return answer//L

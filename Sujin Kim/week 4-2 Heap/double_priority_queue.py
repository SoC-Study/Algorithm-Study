def solution(operations):
    answer = []
    for ele in operations:
        if(ele[0]=='I'):
            answer.append(int(ele[2:]))
        else:
            if(len(answer)==0):
                continue
            if(ele[2] == '1'):
                answer.sort()
                answer.pop()
            else:
                answer.sort(reverse = True)
                answer.pop()
        # print(answer)
    
    if(len(answer)==0):
        return [0, 0]
    return [max(answer), min(answer)]

def solution(operations):
    sorted_lst = []
    prev_op = ""
    
    for op in operations:
        op_str = op.split(" ")
        
        if op_str[0] == "I":
            sorted_lst.append(int(op_str[1]))
        else:
            if len(sorted_lst) == 0:
                continue
            if prev_op == "I":
                sorted_lst.sort()
                
            if op_str[1] == "1":
                sorted_lst.pop()
            else:
                sorted_lst.pop(0)
        
        prev_op = op_str[0]
    
    sorted_lst.sort()
    if len(sorted_lst) == 0:
        answer = [0,0]
    else:
        answer = [sorted_lst[-1], sorted_lst[0]]
        
    return answer

# testcase
operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations)) #[7, 5]
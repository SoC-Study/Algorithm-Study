def solution(operations):
    answer = []
    queue = []
    operations.reverse()
    while operations:
        operation = operations.pop()
        operation = operation.split()
        if operation[0] == "I":
            queue.append(int(operation[1]))
        elif operation[0] == "D" and len(queue) > 0:
            if operation[1] == "1":
                max_index = queue.index(max(queue))
                queue.pop(max_index)
            elif operation[1] == "-1":
                min_index = queue.index(min(queue))
                queue.pop(min_index)
    if len(queue) == 0:
        return [0, 0]
    elif len(queue) == 1:
        return [queue[0], queue[0]]

    else:
        return [max(queue), min(queue)]

    return answer

def solution(priorities, location):
    # queue: list of tuples (index, priority)
    print_queue = []
    for i in range(len(priorities)):
        print_queue.append((i, priorities[i]))
    # print order
    count = 0

    while True:
        # dequeue
        elem = print_queue.pop(0)

        # when queue is empty
        if (len(print_queue) == 0):
            count += 1
            break
        
        # if not the max priority, enqueue again
        if (elem[1] < max(print_queue, key = lambda n: n[1])[1]):
            print_queue.append(elem)
        # print!
        elif (elem[0] == location):
            count += 1
            break
        else:
            count += 1
    
    return count
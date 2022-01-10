def solution(n, computers):
    graph_dict = {}
    for i in range(n):
        graph_dict[i] = []
    for j in range(n):
        for k in range(j+1,n):
            if computers[j][k]:
                graph_dict[j].append(k)
                graph_dict[k].append(j)
    
    all_computers = set([i for i in range(n)])
    answer = 0
    
    while all_computers:
        root = all_computers.pop()
        visited = bfs(graph_dict, root)
        all_computers = all_computers - set(visited)
        answer += 1
    
    return answer


def bfs(graph_dict, root): # O(N^2)
    visited = []
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
            queue.extend(graph_dict[current_node])
    return visited

# testcase
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
print(solution(n, computers))

#[1,1,0]
#[1,1,1]
#[0,1,1]

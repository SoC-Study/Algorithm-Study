def solution(numbers, target):
    root = numbers[0]
    answer = dfs(numbers, root, target, 0, 0) + dfs(numbers, -root, target, 0, 0)
    
    return answer

def dfs(numbers, root, target, depth, answer): # O(2^n)
    if depth + 1 == len(numbers):
        if root == target:
            answer += 1
        return answer
    next_num = numbers[depth + 1]
    
    return dfs(numbers, root + next_num, target, depth + 1, answer) + dfs(numbers, root - next_num, target, depth + 1, answer)

# testcase
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
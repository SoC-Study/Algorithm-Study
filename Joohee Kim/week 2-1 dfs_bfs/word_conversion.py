paths = []

def solution(begin, target, words):
    answer = 0
    graph_dict = {}
    
    if target not in words:
        return 0
    
    all_words = words + [begin]
    for w in all_words:
        graph_dict[w] = []
    
    for w1 in all_words: # O(n^2)
        for w2 in all_words:
            if (w1 != w2) and is_similar(w1, w2):
                graph_dict[w1].append(w2)    
    
    dfs(graph_dict, begin, target, [])

    paths_len = [len(p)-1 for p in paths]
    answer = min(paths_len)
    
    return answer


def is_similar(word1, word2): # O(1)
    same_count = 0
    word_len = len(word1)
    for i in range(word_len):
        if word1[i] == word2[i]:
            same_count += 1
    if same_count >= word_len - 1:
        return True
    return False


def dfs(graph_dict, root, target, visited): # O(n^2)
    visited.append(root)
    
    if root == target:
        paths.append(visited)
        return
    
    for n in graph_dict[root]:
        if n not in visited:
            dfs(graph_dict, n, target, visited[:])

# testcase
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
print(solution(begin, target, words))
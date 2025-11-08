def bfs(n, computers, com, visited):
    queue = []
    queue.append(com)
    visited.append(com)
    result = [com]
    while queue:
        current = queue.pop(0)
        for idx, computer in enumerate(computers[current]):
            if idx not in visited and computer == 1:
                queue.append(idx)
                visited.append(idx)
                result.append(idx)            
    return result
        
    
def solution(n, computers):
    visited = []
    result = []
    for com in range(len(computers)):
        if com in visited:
            continue
        result.append(bfs(n, computers, com, visited))

    return len(result)
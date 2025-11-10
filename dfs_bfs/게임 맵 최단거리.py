from pprint import pprint


def bfs(maps):
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    queue = []
    queue.append([0,0])
    ei, ej = len(maps)-1, len(maps[0])-1
    
    while queue:
        ci, cj = queue.pop(0)
        if [ci,cj] == [ei,ej]:
            break
        for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
            if  (len(maps) > ci+di > -1) and (len(maps[0]) > cj+dj > -1):
                if maps[ci+di][cj+dj] == 1:
                    if visited[ci+di][cj+dj] == 0:
                        queue.append([ci+di,cj+dj])
                        visited[ci+di][cj+dj] = visited[ci][cj] + 1
    
    return visited[ei][ej]


def solution(maps):
    pprint(maps)
    result = bfs(maps)
    if result == 0:
        return -1
    else: 
        return result+1
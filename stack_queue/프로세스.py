from collections import deque

def solution(priorities, location):
    
    priorities = deque(priorities)
    mx = max(priorities)
    cnt = 0
    while priorities:
        if priorities[0] == mx:
            if location == 0:
                cnt +=1
                break
            else:
                cnt +=1
                location -= 1
                priorities.popleft()
                mx = max(priorities)
                
        else:
            if location == 0:
                location = len(priorities)-1
                priorities.append(priorities.popleft())
            else:
                location -= 1
                priorities.append(priorities.popleft())
                
    
    return cnt
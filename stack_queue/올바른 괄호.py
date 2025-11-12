from collections import deque

def solution(s):
    lst = deque()
    
    for c in s:
        if c == '(':
            lst.append(c)
        else:
            if lst:
                lst.popleft()
            else:
                return False
    if lst:
        return False
    
    return True
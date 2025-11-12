from collections import deque

def solution(progresses, speeds):
    result = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        stack = 0
        for progress in progresses:
            if progress >= 100:
                stack += 1
            else: break
        if stack > 0:
            for i in range(stack):
                progresses.pop(0)
                speeds.pop(0)
            result.append(stack)
        
    return result
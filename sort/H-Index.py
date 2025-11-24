from bisect import bisect_left

def solution(citations):
    citations.sort()
    result = 0
    for i in reversed(range(0,10001)):
        if (len(citations) - bisect_left(citations, i)) >= i:
            result = i
            break
    
    return result
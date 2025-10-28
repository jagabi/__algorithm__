def solution(n, times):
    right = n * max(times)
    left = 0
    
    while left < right:
        mid = (right + left) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    
    return left
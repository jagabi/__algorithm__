from collections import deque

def solution(arr):
    result = []
    arr = deque(arr)
    while arr:
        tmp = arr.popleft()
        if arr and tmp == arr[0]:
            continue
        else:
            result.append(tmp)
    return result
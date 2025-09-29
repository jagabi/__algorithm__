import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0

    while scoville:
        if scoville[0] >= K:
            return result
        elif len(scoville) == 1 and scoville[0] < K:
            return -1
        else:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            result += 1

    return result
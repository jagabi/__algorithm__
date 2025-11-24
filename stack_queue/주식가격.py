def solution(prices):
    result = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i,len(prices)-1):
            if prices[j] >= prices[i]:
                result[i] += 1
            else:
                break    
    return result
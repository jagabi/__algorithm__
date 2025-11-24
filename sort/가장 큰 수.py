def solution(numbers):
    result = ''
    numbers = sorted([str(num) for num in numbers],reverse=True, key = lambda x: x*3)
    for num in numbers: result+=num
    
    if int(result) == 0:
        return '0'
    else:
        return result
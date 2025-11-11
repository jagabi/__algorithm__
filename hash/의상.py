def solution(clothes):
    parts = {}
    for cloth in clothes:
        if cloth[1] in parts.keys():
            parts[cloth[1]].append(cloth[0])
        else:
            parts[cloth[1]] = [cloth[0]]
            parts[cloth[1]].append('None')
    
    result = 1
    for part in parts.keys():
        result *= len(parts[part])

    return result-1
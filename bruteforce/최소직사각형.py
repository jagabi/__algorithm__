def solution(sizes):
    w = []
    h = []
    for size in sizes:
        size.sort()
        w.append(size[0])
        h.append(size[1])
    result = max(w)*max(h)
    return result
def solution(numbers, target):
    queue = []

    leaves = []

    leaves.append(numbers[0])
    leaves.append(-numbers[0])

    for i in range(1, len(numbers)):
        queue = []
        for leaf in leaves:
            queue.append(leaf + numbers[i])
            queue.append(leaf - numbers[i])

        leaves = queue[:]

    result = 0
    for leaf in leaves:
        if leaf == target: result += 1

    return result
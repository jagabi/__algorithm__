def solution(array, commands):
    arr = []
    result = []
    for idx, command in enumerate(commands):
        arr.append(array[command[0]-1:(command[1])])
        arr[idx].sort()
        result.append(arr[idx][command[2]-1])
    return result
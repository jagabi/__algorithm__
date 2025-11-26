def solution(answers):
    lst1=[1,2,3,4,5]
    lst2=[2,1,2,3,2,4,2,5]
    lst3=[3,3,1,1,2,2,4,4,5,5]
    result = [0,0,0]
    cnt = 0
    while answers:
        answer = answers.pop(0)
        if lst1[cnt%len(lst1)] == answer: result[0] += 1
        if lst2[cnt%len(lst2)] == answer: result[1] += 1
        if lst3[cnt%len(lst3)] == answer: result[2] += 1
        cnt+=1
    r = []
    for i in range(len(result)):
        if result[i] == max(result):
            r.append(i+1)
    
    return r
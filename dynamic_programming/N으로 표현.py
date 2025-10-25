def solution(N, number):
    if N == number:
        return 1
    
    # dp[i] = N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # N을 i개 이어붙인 수 (5, 55, 555...)
        dp[i].add(int(str(N) * i))
        print(dp)
        
        ## i번 = j번 사용한 결과와 (i-j)번 사용한 결과를 조합
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        # number를 찾으면 바로 리턴
        if number in dp[i]:
            return i
    
    return -1
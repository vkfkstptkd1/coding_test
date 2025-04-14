# dp_금광.py
# n*m의 금광 크기가 있다.
# 각 칸에는 특정 크기의 금이 있다.
# 첫번쨰 열 어느 행에서 출발해 m-1번에 걸쳐 움직인다. 
# 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동한다.
# 결과적으로 채굴자가 얻을 수 있는 최대 금의 크기는?

# 입력 
# T: 테스트 케이스, n,m: NxM
# 출력
# 테스트케이스마다 채굴자가 얻을 수 잇는 금의 최대  크기 출력

# 예시
# 입력
# 2
# 3 4 
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4 
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# 출력
# 19
# 16

# 문제 해결 아이디어
# 금광의 모든 위치에 대해서 다음의 세 가지만 고려
# 1. 왼쪽 위에서 오는 경우, 2. 왼쪽 아래에서 오는경우, 3. 왼쪽에서 오는 경우
# 세 가지 경우 중 가장 많은금을 가지고 있는 경우를 테이블에 갱신해서 문제를 해결한다.
# array[i][j]: i행 j열에 존재하는 금의 양
# dp[i][j]: i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
# 점화식: dp[i][j] = array[i][j] + max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])
# 이 때, 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야 한다.
# 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 된다.
    # 바로 DP 테이블에 초기 데이터를 담아 다이나믹 프로그래밍을 적용할 수 있다.


# 테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보를 입력한다. 
    n, m =map(int,input().split())
    array = list(map(int,input().split()))
    # DP를 위한 2차원 DP 테이블 초기화
    dp = []
    index =0
    for i in range (n):
        dp.append(array[index:index+m])
        index += m
    # DP 진행
    for j in range (1,m):
        for i in range (n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up=0
            else: left_up=dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down =0
            else: left_down=dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    result =0
    for i in range(n):
        result = max(result,dp[i][m-1])
    print(result)




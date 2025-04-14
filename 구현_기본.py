# 구현_기본.py
# 구현이란? 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 알고리즘 대회에서 구현? 풀이는 쉽지만 소스코드로 옮기기 어렵다.
# 구현 유형 예시
# 1. 알고리즘 간단. 코드가 지나칠만큼 길어짐
# 2. 실수 연산을 다루고, 특정 소수점 자리까지 출력해야하는
# 3. 문자열을 특정한 기준에 따라 끊어 처리해야 하는 문제
# 4. 적절한 라이브러리를 찾아서 사용해야 하는 문데

# 일반적으로 알고리즘 문제에서 2차원 공간은 행렬의 의미로 사용된다.
for i in range (5):
    for j in range(5):
        print('(',i,j,')', end=' ')
    print()
# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다.
# 위,아래,왼,오
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#현재위치
x,y=2,2
for i in range(4):
    # 다음위치(위, 아래, 왼,오 차례대로)
    nx=x+dx[i]
    ny=y+dy[i]
    print(nx,ny)
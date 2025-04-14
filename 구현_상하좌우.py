# 구현: 좌표
# [문제]
# 여행가는 n*n 크기의 정사각형 공간 위에 서있다.
# 이 공간은 1*1 크기의 정사각형으로 나누어져있다.
# 가장 왼쪽 위 좌표는 (1,1) 이며, 가장 오른쪽 아래 좌표는 (n,n)에 해당한다.
# 여행가 a는 상,하,좌,우 방향으로 이동할 수 있으며 시작좌표는 항상 (1,1)
# 여행가가 이동할 꼐획이 적힌 꼐획서 L,R,U,D 중 하나의 문자가 반복적으로 적혀있다.
# n*n 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.

# [입력조건]
# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<=N<=100)
# 둘쟤 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<=이동횟수<=100)
# 5
# R R R U D D
# [출력조건]
# 첫째 줄에 여행가가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백을 기준으로 구분하여 출력

# [윤진 아이디어]
# 1. 계획서를 반복해서 
# 2. 일치하는 방향으로 이동시켜 좌표를 증가시킨다.
n = int(input())
arrays = list(input().split())

def yunjin_answer(n,arrays):
    #시작좌표
    x,y=1,1
    nx,ny=x,y
    for array in arrays:

        if array=='L':
            ny=y-1
        elif array=='R':
            ny=y+1
        elif array=='U':
            nx=x-1
        else:
            nx=x+1
        if nx <1 or nx > n or ny <1 or ny >n:
            continue
        # 이동 수행
        x,y=nx,ny
    print(x,y)

def dongbin_answer(n,arrays):
    #시작좌표
    x,y=1,1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # movetype을 정의
    move_types=['U','D','L','R']
    for array in arrays:
        for i in range(len(move_types)):
            if array == move_types[i]:
                nx= x+ dx[i]
                ny= y+ dy[i]
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        x,y=nx,ny
    print(x,y)
    
yunjin_answer(n,arrays)
dongbin_answer(n,arrays)
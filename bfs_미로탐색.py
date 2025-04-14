# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다

import sys
input = sys.stdin.readline

#n 세로, m 가로
# (n,m)까지의 최소 거리를 찾아야 한다.
n,m = map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(n)]


from collections import deque


#상, 하, 좌, 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue =deque()
queue.append((0,0))

while queue:
    x,y=queue.popleft()
    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=n or ny <0 or ny >=m:
            continue
        # 0인경우 무시한다.
        if graph[nx][ny]== 0:
            continue
        if graph[nx][ny]==1:
            graph[nx][ny]= graph[x][y]+1
            queue.append((nx,ny))

print(graph[n-1][m-1])










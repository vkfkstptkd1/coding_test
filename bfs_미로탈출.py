# bfs_미로탈출.py

# 문제
# n*m 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러마리 괴물이 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 1,1이며 미로의 출구는 (n,m)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 잇습니다. 
# 이 때 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 
# 칸을 셀 때 시작칸과 마지막 칸 모두 포함해서 계산합니다.

from collections import deque

# 1. n,m을 입력받는다.
n,m = map(int,input().split())

# 2. 그래프를 입력받는다.
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 3. 이동할 네 가지 방향을 정의한다.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복한다.
    while queue:
        x,y=queue.popleft()
        # 현재위치에서 4가지 방향으로의 위치를 확인한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어난 경우 무시한다.
            if nx<0 or nx>= n or ny<0 or ny >=m :
                continue
            # 괴물인 경우 무시한다.
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리를 기록한다.
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


# 수행 결과 출력
print(bfs(0,0))

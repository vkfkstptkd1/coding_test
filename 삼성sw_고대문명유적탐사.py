
# 1. 유적지에서 3*3 영역을 하나 고른다.
# 2. 그걸 시계방향으로 90,180,270 돌린다.
# > 3*3 회전 함수 만들기
# 3. 같은 숫자의 유물조각이 3개이상이면 유물조각을 세고 없앤다.
# > 유물 찾기 함수 만들기
# 4. 사라진 칸은 벽에 문자들이 들어와서 채워진다.
# > 사라진 칸에 벽 숫자 채우는 함수 만들기
# 5. 다시 유물이 만들어지면 연쇄획득
# --- 위까지가 1번
# 6. 이 모든걸 K번 반복한다. 각 턴마다 얻은 유물점수들을 다 더하면 정답이다.
k,m = map(int,input().split())
graph =[list(map(int,input().split())) for _ in range(5)]
wall_num = list(map(int,input().split()))

def rotate_3x3(graph,c_x,c_y,angle):
    # graph = 유적지 맵, c_x,c_y: 회전중심좌표, angle: 회전 각도
    # 깊은 복사
    new_graph = [row[:] for row in graph]

    # 3x3 범위 계산을 위한 s_x,s_y정의 
    s_x=c_x-1
    s_y=c_y-1

    # 원래 3*3 값 을 저장한 그래프를 그린다. 
    temp = [] 
    for i in range(3):
        row =[]
        for j in range(3):
            row.append(graph[s_x+i][s_y+j])
        temp.append(row)

    # * 회전 함수
    # 세로줄을 거꾸로 읽어서 가로줄로 옮기기
    def rotate_once(mat):
        return [[mat[2-j][i] for j in range(3)] for i in range(3)]

    # 회전할 수
    rotate_count = angle //90
    # 회전 수만큼 회전함수를 돌린다. 
    for _ in range(rotate_count):
        temp = rotate_once(temp)
    

    # 회전한 temp를 new_board에 반영
    for i in range(3):
        for j in range(3):
            new_graph[s_x+i][s_y+j] = temp[i][j]

    return new_graph


# 2단계. 유물 찾기 함수 - 3개 이상 같은 숫자가 붙어있으면 유물이다.
# 유물이 되면 -> 사라지고 0> 점수는 그 조각개수만큼 리턴
# 필요기술: BFS/DFS로 같은 숫자 덩어리 찾기 > dfs-> 성능 문제 생기니까 bfs로 하자.
from collections import deque

def find_and_remove_artifacts(graph):
    n=len(graph)
    
    visited = [[False]*n for _ in range(n)] # 방문 체크
    to_remove = [[False]*n for _ in range(n)] # 지워야 할 곳 표시
    total_score =0 #최종 점수 저장.

    # 상,하,좌,우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    # 보드의 모든 칸을 하나하나 요소를 기준으로 확인해야 한다. 
    for i in range(n):
        for j in range(n):

            # 이미 지워진 칸(=0) / 이미 방문한 칸은 스킵한다
            if graph[i][j] == 0 or visited[i][j]:
                continue
           
            # 새 유물 조각을 발견했을 때, 탐색을 시작한다. 
            q = deque() # 탐색용 큐
            q.append((i,j))
            visited[i][j] =True # 해당 조각은 기준 조각으로 쓰였다. 
            gold =[(i,j)] #유물이 된 조각리스트
            kind =graph[i][j] #유물의 가치 
            
            # 같은 유물을 찾는다.
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx,ny= x+dx[d],y+dy[d]
                    # 좌표가 범위 안에 있으면서 & 방문하지 않았으면서, 가치가 기준 유물의 가치와 같으면
                    if 0<=nx <n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == kind:
                        # 해당 좌표를 방문 처리 한다.
                        visited[nx][ny]=True
                        # 해당 유물의 좌표를 gold에 넣는다. 
                        gold.append((nx,ny))
                        # 해당 좌표를 기준 좌표로 변경한다. 
                        q.append((nx,ny))

            # 만약 얻은 유물의 개수가 3개 이상이면 
            # 1. 가치를 score에 더한다.
            # 2. 지워준다. 
            if len(gold) >=3:                
                total_score+=len(gold)
                for x,y in gold: 
                    to_remove[x][y] = True
            
            # 지운다.
            for i in range(n):
                for j in range(n):
                    if to_remove[i][j]:
                        graph[i][j]=0
    
    return total_score 

# 3. 빈칸 채우기(벽에서 유물 떨어짐)
# "빈 칸을 아래부터, 왼쪽부터, 벽 숫자로 채운다!"
def fill_empty_cells(graph,wall_queue):
    n=len(graph)

    # 빈 셀에 해당하는 좌표를 넣을 배열 
    empty_cells=[]

    # 아래에서 위로 채워서 반대임. 
    for col in range(n):
        for row in range(n-1,-1,-1): # 아래에서 위로 채운다
            if graph[row][col] ==0:
                empty_cells.append((row,col))

    # 정해진 순서대로 채우기: 열 오름차순, 행 내림차순
    empty_cells.sort(key=lambda x: (x[1],-x[0]))

    # 큐를 차례대로 뺀다. 
    for r,c in empty_cells:
        if wall_queue:
            graph[r][c] = wall_queue.popleft()

#4. 연쇄 유물 처리
def chain_artifact_process(graph,wall_queue):
    total_score=0
    while True:
        score = find_and_remove_artifacts(graph)
        if score ==0: # 만약 score가 0이면 반복 끝내기.
            break
        total_score += score
        fill_empty_cells(graph,wall_queue)
    return total_score

# 5. 가장 좋은 회전 찾기
def get_best_rotate(graph,wall_queue):
    n = len(graph)
    max_score = -1
    best_action=(1,1,90) # 초기값 초기화 

    # 모든 경우에 대하여 반복 돌린다. 
    for cx in range(1,n-1): # 중심 x
        for cy in range(1,n-1): # 중심 y
            for angle in [90,180,270]:
                temp_graph = [ row[:] for row in graph]
                temp_wall = deque(wall_queue)
                rotated = rotate_3x3(temp_graph,cx,cy,angle)
                score = chain_artifact_process(rotated,temp_wall)

                if score > max_score:
                    max_score = score
                    best_action = (cx,cy,angle)
    
    return best_action,max_score


# 6. 전체 시뮬레이션 실행
def run_simulation(board, wall_queue, K):
    total_score = []

    for _ in range(K):
        best_action, max_score = get_best_rotate(board, wall_queue)
        if max_score == 0:
            break

        cx, cy, angle = best_action
        board = rotate_3x3(board, cx, cy, angle)
        turn_score = chain_artifact_process(board, wall_queue)
        total_score.append(turn_score) 

    return total_score



wall_queue = deque(wall_num)
score = run_simulation(graph, wall_queue, k)
print("총 점수:", score)









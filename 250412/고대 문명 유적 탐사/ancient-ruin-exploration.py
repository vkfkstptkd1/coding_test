from collections import deque

# ---------- 1. 3x3 회전 함수 ----------
def rotate_3x3(board, cx, cy, angle):
    """
    board: 현재 유적지(5x5 리스트)
    cx, cy: 회전할 3×3 영역의 중심 좌표 (1-indexed)
    angle: 회전 각도 (90, 180, 270)
    
    동작: 
      - (cx, cy)를 중심으로 한 3x3 영역을 시계 방향으로 angle만큼 회전하고,
      - 회전된 결과를 원래 board에 반영한 새 보드를 반환한다.
    """
    # 새 보드를 만들기 (깊은 복사)
    new_board = [row[:] for row in board]
    # 3x3 영역의 시작 인덱스 (0-indexed)
    sx, sy = cx - 1, cy - 1
    
    # 회전할 3x3 영역을 temp에 저장
    temp = [[board[sx + i][sy + j] for j in range(3)] for i in range(3)]
    
    # 90도 시계 방향 회전 함수 (3x3 매트릭스)
    def rotate_once(mat):
        # 새 행의 i번째 값은 기존 열의 역순 값
        return [[mat[2 - j][i] for j in range(3)] for i in range(3)]
    
    # angle에 맞춰 회전 (angle//90번 반복)
    for _ in range(angle // 90):
        temp = rotate_once(temp)
    
    # 회전된 3x3 영역을 new_board에 반영
    for i in range(3):
        for j in range(3):
            new_board[sx + i][sy + j] = temp[i][j]
    
    return new_board

# ---------- 2. 유물 탐색 및 제거 함수 ----------
def find_and_remove_artifacts(board):
    """
    동작:
      - board 내에서 인접(상하좌우)하여 같은 숫자로 이루어진 그룹(유물 조각 그룹)이 
        3개 이상이면, 그 그룹에 속한 칸을 제거(0으로 설정)하고,
      - 점수를 반환한다. (점수 = 제거한 유물 조각의 개수)
    """
    n = len(board)
    visited = [[False]*n for _ in range(n)]
    to_remove = [[False]*n for _ in range(n)]
    total_score = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 모든 칸을 순회하며 같은 숫자 그룹 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 or visited[i][j]:
                continue

            q = deque([(i, j)])
            visited[i][j] = True
            group = [(i, j)]
            kind = board[i][j]

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == kind:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))
            
            # 그룹 크기가 3 이상이면 제거 대상
            if len(group) >= 3:
                total_score += len(group)  # 점수는 조각 개수만큼
                for x, y in group:
                    to_remove[x][y] = True

    # 제거 대상(유물)을 0으로 변경
    for i in range(n):
        for j in range(n):
            if to_remove[i][j]:
                board[i][j] = 0

    return total_score

# ---------- 3. 빈 칸 채우기 함수 ----------
def fill_empty_cells(board, wall_queue):
    """
    동작:
      - board에서 값이 0인 '빈 칸'의 좌표를 찾는다.
      - 빈 칸들은 문제 조건에 따라 **열 기준 오름차순**, 
        같은 열에서는 **행 기준 내림차순(아래부터 위로)** 순서로 채워진다.
      - wall_queue (deque에 저장된 벽 숫자들)에서 하나씩 꺼내 빈 칸에 채운다.
    """
    n = len(board)
    empty_cells = []
    
    # 각 열에 대해, 아래부터 위로 빈 칸 찾기
    for col in range(n):
        for row in range(n - 1, -1, -1):
            if board[row][col] == 0:
                empty_cells.append((row, col))
    # 이미 열 오름차순, 행 내림차순으로 추가되었으므로 sort 필요 없음
    # (만약 순서가 섞이면 아래와 같이 정렬할 수 있음)
    # empty_cells.sort(key=lambda x: (x[1], -x[0]))
    
    # 빈 칸 순서대로 벽 숫자 채우기
    for r, c in empty_cells:
        if wall_queue:
            board[r][c] = wall_queue.popleft()

# ---------- 4. 연쇄 유물 처리 함수 ----------
def chain_artifact_process(board, wall_queue):
    """
    동작:
      - 한 번 회전 후, board에서 유물이 제거되고 빈 칸이 채워지면,
        그 상태에서 다시 유물 제거가 일어날 수 있다.
      - 이 연쇄 과정을 더 이상 제거할 유물이 없을 때까지 반복하며,
        각 반복에서 얻은 점수를 모두 누적하여 반환한다.
    """
    total_score = 0
    while True:
        score = find_and_remove_artifacts(board)
        if score == 0:
            break
        total_score += score
        fill_empty_cells(board, wall_queue)
    return total_score

# ---------- 5. 최적 회전 선택 함수 ----------
def get_best_rotate(board, wall_queue):
    """
    동작:
      - 가능한 모든 3x3 회전 후보(중심 좌표 (cx, cy)와 회전 각도 90,180,270)를 시뮬레이션한다.
      - 각 후보에 대해, 회전 직후 **1차** 유물 제거 점수(즉, find_and_remove_artifacts()로 얻은 점수)를 계산한다.
      - 후보들 중에서 **1차 점수**가 가장 높은 후보를 선택한다.
      - 만약 점수가 같다면, 회전 각도(작은 게 우선), 그 후 열, 행 순으로 작은 것을 선택한다.
    """
    n = len(board)
    candidates = []
    
    for cx in range(1, n - 1):
        for cy in range(1, n - 1):
            for angle in [90, 180, 270]:
                temp_board = [row[:] for row in board]
                # 회전 시뮬레이션
                rotated = rotate_3x3(temp_board, cx, cy, angle)
                # 1차 유물 제거 점수 계산 (연쇄 없이, 한 번만 제거)
                test_board = [row[:] for row in rotated]
                score = find_and_remove_artifacts(test_board)
                if score == 0:
                    continue
                # 후보를 (1차 점수, -angle, -cy, -cx, (cx, cy, angle)) 순으로 저장
                # 음수를 사용하는 이유: 회전 각도는 작을수록 좋으므로, 내림차순 정렬시 작은 값이 우선
                candidates.append((score, -angle, -cy, -cx, (cx, cy, angle)))
    
    if not candidates:
        return None, 0
    # 내림차순 정렬하면 가장 큰 (우선순위) 후보가 첫 번째가 됨
    candidates.sort(reverse=True)
    _, _, _, _, best_action = candidates[0]
    # 반환할 때는 best_action과 1차 점수는 candidates[0][0] (그러나 실제 연쇄 점수는 이후에 계산됨)
    return best_action, candidates[0][0]

# ---------- 6. 전체 시뮬레이션 함수 ----------
def run_simulation(board, wall_queue, K):
    """
    동작:
      - 전체 탐사를 K턴 반복한다.
      - 매 턴마다 get_best_rotate()를 이용해 최적의 3x3 회전 후보를 선택하고,
        선택된 회전을 board에 적용한다.
      - 그리고 체인 연쇄 유물 제거 과정을 실행하여 해당 턴의 총 점수를 얻는다.
      - 모든 턴의 점수(각 턴 별)를 리스트에 담아 반환한다.
    """
    turn_scores = []
    
    for _ in range(K):
        best_action, first_score = get_best_rotate(board, wall_queue)
        if best_action is None:
            break
        cx, cy, angle = best_action
        # 실제 보드에 회전 적용
        board = rotate_3x3(board, cx, cy, angle)
        # 연쇄 유물 제거 및 빈 칸 채우기 과정을 진행하여 해당 턴의 점수 획득
        turn_score = chain_artifact_process(board, wall_queue)
        if turn_score == 0:
            break
        turn_scores.append(turn_score)
    
    return turn_scores

# ---------- 메인 실행 (테스트 케이스) ----------

# 입력 예제:
# 첫 줄: k, m (여기서 m은 문제에서 쓰지 않고, 벽 숫자 개수 제한으로 사용)
# 다음 5줄: 5x5 board
# 마지막 한 줄: 벽에 적힌 숫자들

# 벽 숫자 입력 (총 m개의 숫자가 들어옴)
k,m = map(int,input().split())
board =[list(map(int,input().split())) for _ in range(5)]
wall_nums = list(map(int, input().split()))
wall_queue = deque(wall_nums)

# 전체 시뮬레이션 실행
turn_scores = run_simulation(board, wall_queue, k)
# 출력: 각 턴의 점수를 공백으로 구분하여 출력 (예: 17 3)
print(*turn_scores)

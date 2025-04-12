# 문제를 재현하고 디버그를 돕기 위한 테스트 실행 코드입니다.

from collections import deque

# 이동 거리 계산 함수
def escape(gamers_rc, board, quit_r, quit_c, n):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    changed_gamers_rc = []
    count = 0

    for r, c in gamers_rc:
        min_dist = abs(r - quit_r) + abs(c - quit_c)
        moved = False

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (1 <= nr <= n and 1 <= nc <= n):
                continue
            if board[nr - 1][nc - 1] != 0:
                continue
            new_dist = abs(nr - quit_r) + abs(nc - quit_c)
            if new_dist < min_dist:
                changed_gamers_rc.append((nr, nc))
                count += 1
                moved = True
                break

        if not moved:
            changed_gamers_rc.append((r, c))

    result_rc = []
    for r, c in changed_gamers_rc:
        if r == quit_r and c == quit_c:
            continue
        result_rc.append((r, c))

    return result_rc, count

# 정사각형 찾기
def find_square(n, gamers_rc, quit_r, quit_c):
    candidates = []
    for size in range(2, n + 1):
        for r in range(1, n - size + 2):
            for c in range(1, n - size + 2):
                r2 = r + size - 1
                c2 = c + size - 1
                if not (r <= quit_r <= r2 and c <= quit_c <= c2):
                    continue
                for gr, gc in gamers_rc:
                    if r <= gr <= r2 and c <= gc <= c2:
                        candidates.append((size, r, c))
        if candidates:
            break
    candidates.sort(key=lambda x: (x[1], x[2]))
    return candidates[0]

# 회전 함수
def rotate_board(board, square, gamers_rc, quit_r, quit_c):
    size, r, c = square
    r -= 1
    c -= 1
    temp = [row[c:c + size] for row in board[r:r + size]]
    rotated = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated[j][size - 1 - i] = temp[i][j]
    for i in range(size):
        for j in range(size):
            board[r + i][c + j] = max(0, rotated[i][j] - 1)
    new_gamers_rc = []
    for gr, gc in gamers_rc:
        if r <= gr - 1 < r + size and c <= gc - 1 < c + size:
            rel_r = (gr - 1) - r
            rel_c = (gc - 1) - c
            new_r = r + rel_c + 1
            new_c = c + (size - 1 - rel_r) + 1
            new_gamers_rc.append((new_r, new_c))
        else:
            new_gamers_rc.append((gr, gc))
    if r <= quit_r - 1 < r + size and c <= quit_c - 1 < c + size:
        rel_r = (quit_r - 1) - r
        rel_c = (quit_c - 1) - c
        quit_r = r + rel_c + 1
        quit_c = c + (size - 1 - rel_r) + 1
    return new_gamers_rc, quit_r, quit_c

# 시뮬레이션 함수
def simulate(n, board, gamers_rc, quit_r, quit_c, k):
    total_move = 0
    for _ in range(k):
        gamers_rc, move = escape(gamers_rc, board, quit_r, quit_c, n)
        total_move += move
        if not gamers_rc:
            break
        square = find_square(n, gamers_rc, quit_r, quit_c)
        gamers_rc, quit_r, quit_c = rotate_board(board, square, gamers_rc, quit_r, quit_c)
    print(total_move)
    print(quit_r, quit_c)

    

# n: 미로의 크기 4<=n<=10
# m: 참가자 수  1<=m<=10
# k: 게임 시간 1<=k<=100
n,m,k = map(int,input().split())

# board; 0: 빈칸; 1-9: 벽,내구도
board = [list(map(int,input().split())) for _ in range(n)]

# 참가자의 좌표
gamers_rc = [tuple(map(int,input().split())) for _ in range (m)]

# 첫 출구의 좌표
s_quit_r,s_quit_c= map(int,input().split())
     

simulate(n, board, gamers_rc, s_quit_r, s_quit_c, k)

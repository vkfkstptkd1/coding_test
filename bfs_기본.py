# bfs_기본.py
# bfs: 너비 우선 탐색. 가까운 노드부터 우선적으로 탐색한다. 
# 과정
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리 
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문을 처리
# 3. 더이상 2번의 과정을 수행할 수 없을때까지 반복

from collections import deque

#각 노드가 연결된 정보를 표현
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited =[False] * 9

def bfs(graph,start,visited):
    # 큐 구현을 위해 deque를 사용한다.
    queue = deque([start])
    print("queue1:",  queue)

    # 현재 큐를 방문처리 한다.
    visited[start] = True
    # 큐가 빌 때 까지 반복한다.
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력한다.
        v = queue.popleft()
        print(v, end= ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
            print("queue2:",  queue)


bfs(graph,1,visited)
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
# 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

n,m,v= map(int,input().split())

# 처음 그래프를 노드의 개수 만큼 초기화 한다.
graph =[[] for _ in range(n+1)]

# ** 간선의 개수만큼 정보를 입력받는다.
for _ in range(m):
    a,b=map(int,input().split())
    # a에 헤당하는 자리에 b를 삽입한다.
    graph[a].append(b)
    # b에 헤당하는 자리에 b를 삽입한다.
    graph[b].append(a)

# 작은 번호부터 방문하기 위한 정렬을 수행한다. 
for g in graph:
    g.sort()



# dfs
# 재귀로 구현한다.
# 시작노드와, 해당 노드의 방문 정보를 매개로 받는다.

def dfs(v,visted):
    # v에 해당하는 노드를 방문 처리 한다.
    visted[v]=True
    # 방문한 노도를 프린트한다.
    print(v, end=' ')
    # v를 해당 그래프를 탐색하며 방문하지 않은 노드로 변경한다.
    for neighbor in graph[v]:
        # 만약 해당 노드를 방문하지 않는다면
        if not visted[neighbor]:
            # dfs 함수를 실행한다.
            dfs(neighbor,visted)



# bfs
from collections import deque
def bfs(v):
    # 첫 노드를 queue에 넣는다.
    # 해당 노드를 방문처리 하고 quee에서 뺀다.
    visited = [False]*(n+1)
    queue = deque([v])
    visited[v]=True
    # queue가 존재할 때까지 반복한다.
    while queue: 
        # 큐에서 노드를 뺀다. 
        node = queue.popleft()
        # 해당 노드를 프린트한다.
        print(node, end = ' ')
        # 해당 노드에 연결된 노드를 방문한다.
        for neighbor in graph[node]:
            # 연결 노드에 방문하지 않았다면
            if not visited[neighbor]:
                # 해당 노드를 방문했다고 처리한후,
                visited[neighbor]=True
                # queue에 집어넣는다 
                queue.append(neighbor)


dfs_visted=[False]*(n+1)
dfs(v, dfs_visted)
print()  # 줄바꿈
# BFS 결과 출력
bfs(v)



# # 입력받는다. 
# n,m,v = list(map(int,input().split()))

# # 그래프 정보를 초기화한다.
# # 이걸 하는 이유는 그래프의 n번째 인덱스에 n의 노드에 연결된 노드를 정의하기 위함이다.
# graph = [[] for _ in range(n+1)]

# # 그래프 정보를 입력받고, 해당 연결 정보를 각각 인덱스에 맞게 저장한다.
# for i in range (m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 작은것 부터 순회한다고 하였으니, 연결노드 정보를 오름차순으로 정렬한다.
# for g in graph:
#     g.sort()


# # dfs를 수행한다.
# # dfs는 연결 노드를 방문하면서, 연결된 노드가 방문처리 되지 않앗으면 바로 방문해서 방문처리해버리는 구조다. 
# # 그러므로 방문에 대한 정보가 초기화 되어야 한다.
# dfs_visited=[False]*(n+1)
# def dfs(v,visited):
#     visited[v]=True
#     print(v, end= ' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i,visited)

# # bfs를 수행한다.
# # bfs는 인접 노드를 가장 우선적으로 방문한다.
# # 각 노드를 방문하면서 큐에 넣고 방문 처리되면 바로 빼서 고려하지 않는다. 
# from collections import deque
# def bfs(v):
#     bfs_visited=[False]*(n+1)
#     # 초기 노드를 큐에 넣는다.
#     queue = deque([v])
#     bfs_visited[v]=True
#     # 큐가 없어질 때가지 반복한다.
#     while queue:
#         # 큐에서 뺀 후, 프린트할 노드에 저장한다. 
#         node = queue.popleft()
#         # 프린트한다.
#         print(node, end= ' ')
#         # 프린트 한 노드에 인접 노드를 돌며, 
#         for n in graph[node]:
#             # 방문하지 않았을 경우,
#             if not bfs_visited[n]:
#                 #방문으로 바꾼 후, 
#                 bfs_visited[n]=True
#                 # 큐에서 뺄 노드로 삽입한다. 
#                 queue.append(n)

# def bfs(v):
#     visited=[False] * (n+1)
#     queue = deque([v])
#     visited[v]=True
#     while queue:
#         node = queue.popleft()
#         print(node, end= ' ')
#         for n in graph[node]:
#             if not visited[n]:
#                 visited[n] = True
#                 queue.append(n)

    


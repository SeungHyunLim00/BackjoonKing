#다리만들기 2

# 섬 - 다리 연결
# NxM
# 다리는 바다에만 건설할 수 있다
# 다리의 길이는 2 이상이어야 한다.   방향은 중간에 바뀔 수 없다. 세로 또는 가로.

# MST 문제
# Kruskal (엣지 선택) vs Prim (노드 선택)
# minmax 하려다 ㅌㅌ -> 엣지 제대로 생각 x

from collections import deque
from heapq import heappush, heappop


# TODO 0. 기초공사
DEBUG = False
inrange = lambda x, y : bool(0<=x<N and 0<=y < M)
dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
INF = int(1e9)

def find(a:int):
    if reps[a] != a:
        reps[a] = find( reps[a])
        return reps[a]
    return a

def union(a, b):
    repa = find(a)
    repb = find(b)
    reps[repb] = repa

# TODO 1. 함수들
def bfs():

    visited = [[0]*M for _ in range(N)]
    g_num = 1
    q = deque()
    for x in range(N):
        for y in range(M):
            if visited[x][y] or not matrix[x][y]:
                continue

            q.append((x, y))
            visited[x][y] = g_num
            while q:
                cur_x, cur_y = q.popleft()
                for dx, dy in dxdy:
                    nx, ny = cur_x+dx, cur_y + dy
                    if inrange(nx,ny) and not visited[nx][ny] and matrix[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = g_num
            g_num += 1

    return visited, g_num - 1

def get_edges(): # a섬과 b 섬 사이 최단 거리 찾기
    edges = []
    for x in range(N):
        for y in range(M):
            if not group[x][y]:
                continue
            # 섬이다. 시작
            start = group[x][y]

            for dx, dy in dxdy:
                cur_x, cur_y = x, y
                dist = 0
                while True:

                    nx, ny = cur_x+dx, cur_y+dy

                    dist += 1
                    if not inrange(nx,ny):
                        break
                    if group[nx][ny]:
                        if group[nx][ny] == start:
                            break
                        else:
                            dist = dist -1
                            if dist > 1:
                                heappush(edges, (dist, start, group[nx][ny] ))
                            break
                    else:
                        cur_x, cur_y = nx,ny

    if DEBUG:
        print(f"edges ")
        print(edges)
    return edges


# TODO 3. 메인 실행부
N, M = map(int, input().split())
matrix = []

for x in range(N):
    matrix.append(list(map(int, input().split())))

group, g_num = bfs()
if DEBUG:
    for row in group:
        print(*row)


reps = [i for i in range(g_num+1)] # 역시 0번쨰는 사용하지 않는다.

edges = get_edges()

total_dist = 0
while edges:
    dist, landA, landB = heappop(edges)
    if find(landA) == find(landB):
        continue
    # 같은 집합 아님
    total_dist += dist
    union(landA, landB)
    print(f"we choose {landA}, {landB} with dist {dist}") if DEBUG else 0

cri = find(reps[1])

for x in range(1, g_num+1):
    if find(x) != cri:
        print("-1")
        break
else:
    print(total_dist)
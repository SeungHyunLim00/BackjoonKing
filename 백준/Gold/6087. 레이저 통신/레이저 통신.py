# 레이저 통신
#09:50 독해 시작
# 10:02 구현 시작 - 0-1bfs와 다익 두가지로 풀어본다.
# 디버깅 : 아놔 벽 또 생각 안했네
# 아 visited를 한 칸에 대해서 하면 안된다.
# 들어오는 방향 d 가 중요함.
# 10:15 1차 제출 통과
# 0-1 bfs로 구현해봄
# if cr == er and cc == ec:
#     print(cost)
#     break
# 일케 하면 안되는듯
# 아니 0-1로 안되자너. 무조건 한

drdc = [(1,0),  (0,1), (-1,0),(0,-1)]
inrange= lambda r, c : bool(0<=r<H and 0<=c<W)
W, H = map(int, input().split())


matrix = []
sr, sc, er, ec = -1,-1,-1,-1
INF = int(1e9)
for r in range(H):
    matrix.append(list(input().strip()))
    for c, val in enumerate(matrix[-1]):
        if val == "C":
            if sr != -1:
                er, ec = r, c
            else:
                sr, sc = r, c


# er, sr = sr, er
# ec, sc = sc, ec
# print(f"{sr, sc} -> {er, ec}")
# 방법 1

from heapq import heappop, heappush


visited = [[[INF,INF, INF, INF] for _ in range(W)] for _ in range(H)]
hq = [(-1, -1, sr, sc)] # cost, d, r, c
visited[sr][sc] = [0,0,0,0]

while hq:
    cost, cd, cr, cc = heappop(hq)
    #print(f"at {cr, cc} => cost{cost} with {cd}")
    if cr == er and cc == ec:
        break
    if visited[cr][cc][cd] < cost:
        continue
    for d, (dr, dc) in enumerate(drdc):
        nr, nc = cr + dr, cc + dc
        if not inrange(nr,nc):
            continue
        if matrix[nr][nc] == "*":
            continue

        ncost = cost + 1 if cd != d else cost
        if visited[nr][nc][d] <= ncost:
            continue
        heappush(hq, (ncost, d, nr, nc))
        visited[nr][nc][d] = ncost

print(min(visited[er][ec]))
'''
from collections import deque
q = deque()
q.append((sr, sc, -1, -1)) # r, c, d, cost

dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]

while q:
    cr, cc, cd, cost = q.popleft()
    if cd != -1 and cost > dist[cr][cc][cd]: continue  # 낡은 항목 버리기
    if (cr, cc) == (er, ec): print(cost); break  # 처음 꺼낼 때 확정


    for d, (dr, dc) in enumerate(drdc):
        nr, nc = cr + dr, cc + dc

        if not inrange(nr,nc):
            continue

        if matrix[nr][nc] == "*": continue
        if cd == d:
            if dist[nr][nc][d] <= cost:
                continue
            q.appendleft((nr, nc, d, cost))
        else:
            if dist[nr][nc][d] <= cost + 1:
                continue
            dist[nr][nc][d] = cost + 1
            q.append((nr, nc, d, cost + 1))
'''
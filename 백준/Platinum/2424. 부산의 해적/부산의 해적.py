# 부산의 해적
# 시간별로 뭐 이런걸 해보다가 그냥 고돌고소미처럼 여러 for문 돌기로 함
# NxM 크기
# '어떻게 움직이건 관계 없이'
# dfs인가?
# 다시, 갈아엎자. 해적이 갈 수 있는 곳을 time으로 표시 -> 어차피 계속 죽칠 수 있음.
from collections import deque
DEBUG = False

N, M = map(int, input().split())

sr, sc, pr, pc = -1, -1, -1, -1
matrix = []
for r in range(N):
    matrix.append(input())
    for c, val in enumerate(matrix[-1]):
        if val == "Y":
            sr, sc = r, c
        elif val == "V":
            pr, pc = r, c
if DEBUG:
    matrix[sr] = matrix[sr][:sc] + "." + matrix[sr][sc+1:] # 디버깅용
    matrix[pr] = matrix[pr][:pc] + "." + matrix[pr][pc+1:]
    for row in matrix:
        print(*row)
    print(f"start {sr, sc} and pirate:  {pr, pc} ")

drdc = [(1,0), (-1,0), (0,1), (0,-1)]

def see(sr, sc, time_):
    for dr, dc in drdc:
        cr, cc = sr, sc
        while True:
            if dist_map[cr][cc] <= time_: return True
            nr, nc = cr + dr, cc + dc
            if not (0<=nr<N and 0<=nc<M) : break
            if matrix[nr][nc] == "I": break
            cr, cc = nr, nc
    return False

INF = int(1e9)
dist_map = [[INF]*M for _ in range(N)]
q = deque()
q.append((pr, pc))
dist_map[pr][pc] = 0

while q:
    cr, cc = q.popleft()
    for dr, dc in drdc:
        nr, nc = cr + dr, cc + dc
        if not (0 <= nr < N and 0 <= nc < M): continue
        if matrix[nr][nc] == "I": continue
        if dist_map[nr][nc] != INF: continue
        dist_map[nr][nc] = dist_map[cr][cc] + 1
        q.append((nr,nc))

# for row in dist_map:
#     for val in row:
#         if val == INF : print("INF", end =" ")
#         else: print(f"{val:3d}", end = " ")
#     print()

def solve():
    q = deque()
    q.append((sr, sc))
    visited = [[False]*M for _ in range(N)]
    visited[sr][sc] = True

    time_ = 0
    while q:
        for _ in range(len(q)):
            cr, cc = q.popleft()
            #print(f"{cr, cc} at time {time_}")
            if matrix[cr][cc] == "T":
                return True

            for dr, dc in drdc:  # 수아 이동
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < N and 0 <= nc < M): continue
                if matrix[nr][nc] == "I": continue
                if visited[nr][nc] : continue
                if see(nr, nc, time_+1): continue
                q.append((nr,nc))
                visited[nr][nc] = True
        time_ += 1
    return False

print("YES") if solve() else print("NO")
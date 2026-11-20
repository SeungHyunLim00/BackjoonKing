# 다리만들기
# 구상 안함. 바로 풀 수 있을듯
# 10:43 - 11:01 구현 18분
# 1차 제출 통과

from collections import deque

N = int(input())
drdc = [(1,0),(-1,0),(0,1),(0,-1)]
inrange = lambda r, c : bool(0<=r<N and 0<=c<N)

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split()))) # 0은 바다, 1은 육지

q = deque()
group = [[0]*N for _ in range(N)]
gnum = 0
for r in range(N):
    for c in range(N):
        if group[r][c] or matrix[r][c] == 0:
            continue
        gnum += 1
        q.append((r,c))
        group[r][c] = gnum
        while q:
            cr, cc = q.popleft()
            for dr, dc in drdc:
                nr, nc = cr+dr, cc + dc
                if not inrange(nr,nc):
                    continue
                if group[nr][nc]:
                    continue
                if matrix[nr][nc] == 1:
                    q.append((nr,nc))
                    group[nr][nc] = gnum

# for row in group:
#     print(*row)
min_bridge = int(1e9)
vset = set()
for r in range(N):
    for c in range(N):
        if not group[r][c]:
            continue
        # start 하기
        st_g = group[r][c] # 출발 gnum
        vset.clear()
        q.clear()
        q.append((r,c, 0)) # 재사용, dist
        vset.add((r,c))
        while q:
            cr, cc, cdist = q.popleft()
            if group[cr][cc] and group[cr][cc]  != st_g:
                min_bridge = min(min_bridge, cdist-1)
                break
            for dr, dc in drdc:
                nr, nc = cr+dr, cc + dc
                if not inrange(nr,nc):
                    continue
                if group[nr][nc] == st_g:
                    continue
                if (nr,nc) in vset:
                    continue
                q.append((nr,nc,cdist+1))
                vset.add((nr,nc))

print(min_bridge)
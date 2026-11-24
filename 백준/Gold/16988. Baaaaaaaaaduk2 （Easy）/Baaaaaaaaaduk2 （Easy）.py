# 바ㅏㅏㅏㅏㅏ둑
# 16: 40 독해 시작
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
drdc = [(1,0), (-1,0), (0,1), (0,-1)]
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
    # 0 빈, 1 나, 2 상대
empty = []
q = deque()
group = [[0]*M for _ in range(N)]
gnum = 0
g_empty = [None]
g_cnt = [None]
for r in range(N):
    for c in range(M):
        if group[r][c] : continue
        if matrix[r][c] == 0: empty.append((r,c)); continue
        elif matrix[r][c] == 1 : continue
        gnum += 1
        q.append((r,c))
        group[r][c] = gnum
        g_empty.append(set())
        cnt = 0
        while q:
            cr, cc = q.popleft()
            cnt += 1
            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc
                if not (0<=nr<N and 0<=nc<M) : continue
                if group[nr][nc] : continue
                if matrix[nr][nc] == 0:
                    g_empty[-1].add((nr,nc))
                elif matrix[nr][nc] == 2:
                    q.append((nr,nc))
                    group[nr][nc] = gnum
        g_cnt.append(cnt)

# for gnum, lst in enumerate(g_empty):
#     if gnum == 0:continue
#     print(f"for {gnum} len {g_cnt[gnum]}: {lst}")

max_ans = 0
for rc1, rc2 in combinations(empty, 2):
    temp = 0
    for gnum, e in enumerate(g_empty):
        if gnum == 0 or len(e) > 2: continue
        if len(e) == 2:
            if rc1 in e and rc2 in e:
                temp += g_cnt[gnum]
        else:
            if rc1 in e or rc2 in e:
                temp += g_cnt[gnum]
    max_ans = max(max_ans, temp)

print(max_ans)
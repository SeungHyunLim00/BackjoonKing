# 군대 탈출
# 아는 맛이라 바로 ㄱ
# 최소 레벨 -> max Lv 하면서
# 다익식 접근 필요
# 아 타일을 뛰어넘는 도중에 방향을 바꿀 수 없다
# d 가 0 이라서
# 아 방향도 중요함 -> visit 관리
from collections import deque
from collections import defaultdict


INF = int(1e9)
drdc = [(1,0),(-1,0),(0,1),(0,-1)]
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
visited = [[[INF,INF] for _ in range(M)]for _ in range(N)]

q = deque()
q.append((0,0,matrix[0][0],0))
vdict = defaultdict(lambda : INF)
for i in range(1,5):
    vdict[(0,0,0,i)] = matrix[0][0]

while q:
    cr, cc, maxLv, skip = q.popleft()
    #print(f"at {cr, cc} skip {skip} | max {maxLv}")
    if cr == N-1 and cc == M-1 :
        continue

    for d, (dr, dc) in enumerate(drdc, 1):
        nr,nc = cr + dr, cc + dc
        if not (0<=nr<N and 0<=nc<M): continue # 만약 썼는데 슝 날라가면?

        nmaxLv = max(maxLv, matrix[nr][nc])
        if skip > 0 : #직전에 썼다
            if d != skip: continue
            if vdict[(nr,nc,1,d)]<= nmaxLv :
                continue
            q.append((nr,nc,nmaxLv, - skip))
            vdict[(nr,nc,1,d)] = nmaxLv
        elif skip < 0: # 이전에 씀
            if vdict[(nr,nc,1,d)] <= nmaxLv :
                continue
            q.append((nr,nc,nmaxLv, skip))
            vdict[(nr,nc,1,d)] = nmaxLv
        else: # skip = 0

            if vdict[(nr,nc,0,d)] > nmaxLv: # 안씀
                q.append((nr, nc, nmaxLv, 0))
                vdict[(nr,nc,0,d)] = nmaxLv
            # 다음칸에 쓸거임
            #if nmaxLv > maxLv : # 이렇게 해도 되나? 그래야 쓰는 의미가
            if not (nr == N-1 and nc == M-1) and vdict[(nr,nc,1,d)] > maxLv:
                q.append((nr, nc, maxLv, d))
                vdict[(nr,nc,1,d)] = maxLv


ans  = INF

for i in range(1,5):
    ans = min(ans, vdict[(N-1, M-1, 0, i)])
for i in range(1, 5):
    ans = min(ans, vdict[(N - 1, M - 1, 1, i)])

print(ans)
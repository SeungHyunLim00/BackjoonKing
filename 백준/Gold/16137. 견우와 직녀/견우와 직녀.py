# 견우와 직녀
# 구상 19:07 ~ 19:22
#
# 19:43 디버깅 - time_ + 1 로. 오작교 위에 있는 시간을 나눠야함.
# -> 이거 고쳤을 때 달라지는 점 생각해보자. 음....없는듯??
# 검토 5분 - 쭉 읽기, 20으로 나누는게 맞는지 생각해보기
# 1차 제출 실패 -> 왜지?
# 의심가는 부분 ) 오작교 candidate 검사
# 아 헐 그 뭐냐 오작교 건설한것도 절벽인데 -> matrix[nr][nc] != 1:
# 2차제출 실패
# 아 오작교 위에서 대기할 수도 있겠구나
# nr, nc시에 , continue 하는 조건 동일하게 맞출것

from collections import deque

INF = int(1e9)
drdc = [(0,-1), (-1,0), (0,1), (1,0)]

N, PERIOD = map(int, input().split())# M 헷갈려
inrange = lambda r, c : bool(0<=r<N and 0<=c<N)
candidates = []

matrix = []
for r in range(N):
    matrix.append(list(map(int, input().split())))

for r in range(N):
    for c, val in enumerate(matrix[r]):
        if val == 0:
            nei = []
            for d, (dr, dc) in enumerate(drdc):
                nr, nc = r + dr, c + dc
                if not inrange(nr,nc): continue
                if matrix[nr][nc] != 1:
                    nei.append(d)
            if len(nei) > 2 : continue
            else : # 2 이하
                if len(nei) == 2:
                    if abs(nei[0] - nei[1]) != 2: continue # 반대관계(같은길) ㄴㄴ
                candidates.append((r,c))

def bfs():
    q = deque()
    q.append((0,0,False)) # state, 이전에 오작교 건넜는지

    visited = [[0]*N for _ in range(N)]
    visited[0][0] |= 1<<0  # 비트로 1칸당 0~19 저장

    time_ = 0
    # 가만히 있을 때도 빼먹지말고
    while q:

        for _ in range(len(q)):
            cr, cc, state = q.popleft()
            if cr == N-1 and cc == N-1:
                return time_

            ntime_bit = 1<<((time_ + 1)%20)

            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc
                if not inrange(nr,nc): continue
                val = matrix[nr][nc]
                if val == 0 : continue
                elif val == 1:
                    if visited[nr][nc] & ntime_bit: continue
                    q.append((nr, nc, False))
                    visited[nr][nc] |= ntime_bit
                else: # 오작교임
                    if state: continue # 연속 못건넘
                    if (time_+1) % val != 0: continue # 주기아님, 못감
                    if visited[nr][nc] & ntime_bit : continue
                    q.append((nr, nc, True))
                    visited[nr][nc] |= ntime_bit

            # 아마? 제자리 기다리는 것도 - 안빼묵음
            if matrix[cr][cc] > 1 : continue
            if visited[cr][cc] & ntime_bit: continue
            q.append((cr, cc, False))
            visited[cr][cc] |= ntime_bit
        time_ += 1

    return INF # 여기 오면 안됑 아 아닌 케이스도


min_time = INF
for cr, cc in candidates:
    matrix[cr][cc] = PERIOD
    res = bfs()
    min_time = min(min_time, res)
    matrix[cr][cc] = 0

print(min_time)
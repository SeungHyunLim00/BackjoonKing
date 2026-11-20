# 불켜기 (시간 내 x)
# 19:07 ~ 19:23 구상 16분
# 일단 bfs로 하는데... 자신이없네
# 1. 공복 : 100x100x100 (상태 bit-> list로 저장 후 모든 node 방문한다 쳐)
# 2. 시복 -> bfs면
# ㄴㄴ 다시 재구상함 possible을 공유해도 괜찮겠구나. 어차피 어느 방향을 가건 중요한건 dist가 아니다.
# 한개의 상태 공유? union-find? 2D matrix도 그래프다. 연결만 되어있으면
# 원복을 안하는 dfs?
# 방 최대 개수(구하는 것)은 1개. 자명해임

# 19:29 구현 시작
# 19:41 정답은 나왔는데... 쎄 하다 검증? ㄱㄱ
# 100 20000 테케 -> 시간 절대 x
# 19:55 light matrix와 vset을 분리. 손봄
# 19:57 1차 틀림 92/100
# 방문 가능한 set에
# 20:09 2차 제출 : 와 1개 틀림 wtf 길어서 복붙도 못함


# 11:10 ~ 11:15 디버깅
from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
# 기초공사
N, M = map(int, input().split()) # NxN이다 정신차려
inrange = lambda r, c : bool(0<=r<N and 0<=c<N)
drdc = [(1,0), (-1,0), (0,1), (0,-1), (0,0)] # 본인도 더해준다

adj = defaultdict(list) # 헿
for _ in range(M): # 20000개, 안터진다.
    sr, sc, er, ec = map(lambda t: int(t) - 1 , input().split()) # 변환 안한다. 가상의 matrix로 함.
    adj[(sr,sc)].append((er, ec))

light = [[False]*N for _ in range(N)]

poss = set()
visited = set([(0,0)])
light[0][0] = True
q = deque()
q.append((0,0))

while q:
    cr, cc = q.popleft()

    for dr, dc in drdc:
        nr, nc = cr + dr, cc + dc
        if not inrange(nr,nc): continue # 할필요 없긴 한데 set 터질까바
        poss.add((nr, nc)) # 방문 가능한
        if light[nr][nc] == True and (nr,nc) not in visited:
            q.append((nr,nc))
            visited.add((nr,nc))

    for nr, nc in adj[(cr, cc)]:
        light[nr][nc] = True
        if (nr,nc) in visited:
            continue

        if (nr,nc) in poss:
            visited.add((nr,nc))
            q.append((nr,nc))


print(sum(sum(row) for row in light))

# 유령의 집 탈출하기
#09:11 독해 시작 ~ 09:14 구현 시작
# 가시거리 벽이나 다른 유령 -> 안변한다 -> 초기에 한번 구해놓기
# 아 ghost 별로 dict 하면 될 줄 알았는데 흠 matrix로 저장해야하나?
# GHOST 최대가 몇인지 안나와ㅣㅆ네
# 아놔 ㄱ또 dr을 dc로 씀 왜이러냐 -> 디버깅 5분\
# see_ma ㄱ만드는데까지 09:33
# visited를 matrix 로 했다가 계속 가만히 있어도 된다는걸 깨달음 -> 이러면 무한하게 가만히 있는디
# 아 4초 이상 기다려도 안되면 안되는거군
# 디버깅 : 맨 아래 이동 안할때 nr,nc를 넣어서 누수
# 아 가만히 있을 때도 유령 시야가 오는지 체크해줘야함
# 1차제출실패 => 아놔 복붙해서 cr, cc를 nr, nc로 씀
from collections import deque
N, M = map(int, input().split())

drdc = [(0,1), (1,0), (0,-1), (-1,0)]
inrange = lambda r, c : bool(0<=r<N and 0<=c<M)

sr, sc, er, ec = map(lambda t: int(t)-1, input().split()) # 1-base -> 0-based
ghosts = []
matrix = []
for r in range(N):
    matrix.append(list(input().strip()))
    for c, val in enumerate(matrix[-1]):
        if val.isdigit():
            ghosts.append((r, c, int(val)))
            matrix[r][c] = "G" # string으로 통일해줌

see_ma = [[0]*M for _ in range(N)]
# 초기 조건잡기
for r, c, d in ghosts:
    for i in range(4):
        cr, cc = r, c
        nd = (d + i)% 4
        dr, dc = drdc[nd]
        while True:
            see_ma[cr][cc] |= 1<<i # i초 일때 못지나감
            nr, nc = cr + dr, cc + dc
            if not inrange(nr,nc): break
            if matrix[nr][nc] in ("G", "#") : break
            cr, cc = nr, nc

# for row in see_ma:
#     for val in row:
#         print(f"{bin(val)[2:]:5s}", end = " ")
#     print()

ans, dist = -1, 0
q = deque()
q.append((sr, sc))
visited = [[[False, False, False, False] for _ in range(M)] for _ in range(N)]
visited[sr][sc][0] = True

while q:
    for _ in range(len(q)):
        cr, cc = q.popleft()
        if cr == er and cc == ec : ans = dist; break
        nt = (dist+1) % 4
        for dr, dc in drdc:
            nr, nc = cr + dr, cc + dc
            if not inrange(nr,nc) or visited[nr][nc][nt]:continue
            if matrix[nr][nc] in ("#", "G") : continue
            if see_ma[nr][nc] & 1<<nt : continue # 유령이 보고있음
            q.append((nr,nc))
            visited[nr][nc][nt] = True

        if visited[cr][cc][nt]: continue
        if see_ma[cr][cc] & 1 << nt: continue # 이것도 해줘야함

        visited[cr][cc][nt] = True
        q.append((cr, cc))

    if ans == -1: dist += 1
    else: break

print(ans) if ans != -1 else print("GG")
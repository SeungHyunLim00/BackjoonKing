# 와드
# 10:06 독해시작
# 불켜기 류인가? 했다가 더 쉬운듯
# flood fill로 구역 나눠주고
# wad 한 곳의 group만 신경
# 마지막에 사람 시야 신경써서 r,c 순회하며 프린트하면 될듯
# 10:12 구현시작
from collections import deque

drdc = [(1,0), (-1,0), (0,1), (0,-1)]
R, C = map(int, input().split())
inrange = lambda r, c : bool(0<=r<R and 0<=c<C)
trans = {"U": 1, "D":0, "L":3, "R":2}

matrix = []
for _ in range(R):
    matrix.append(input()) # 어차피 group 만드는 용이므로 strip 안한다

groups = [[0]*C for _ in range(R)]
q = deque()
gnum = 0
for r in range(R):
    for c in range(C):
        if groups[r][c]: continue
        gnum += 1
        q.append((r,c))
        groups[r][c] = gnum
        while q:
            cr, cc = q.popleft()
            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc
                if not inrange(nr,nc): continue
                if groups[nr][nc]: continue
                if matrix[cr][cc] != matrix[nr][nc] : continue
                q.append((nr,nc))
                groups[nr][nc] = gnum

# for row in groups:
#     print(*row)
wad = set()
cr, cc = map(lambda t: int(t)-1, input().split())
for order in input():

    if order == "W":
        wad.add(groups[cr][cc])
        continue
    dr, dc = drdc[trans[order]]
    cr, cc  = cr + dr, cc + dc

mysee = set()
mysee.add((cr,cc))
for dr, dc in drdc:
    nr, nc = cr + dr, cc + dc
    mysee.add((nr,nc)) # 어차피 범위 벗어난거 내가 안줌

for r in range(R):
    for c in range(C):
        if (r,c) in mysee:
            print(".", end = "")
        elif groups[r][c] in wad:
            print(".", end = "")
        else:
            print("#", end = "")
    print()
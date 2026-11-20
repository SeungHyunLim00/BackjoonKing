# 움직이는 미로 탈출
# 10:50 독해 시작
# 10:55 구현
# 11:08 예제 5개 맞
# 11:09 1차 제출 통과
from collections import deque
from itertools import product

time_ma = [] # n초의 matrix
temp = []
for _ in range(8):
    temp.append(input()) # string으로 저장해도 된다.
time_ma.append(temp[:])# 0초

for time_ in range(8):
    temp = ["."*8] + temp[:-1]
    time_ma.append(temp[:])

# for tiem_ in range(9):
#     print(f"at time {tiem_}")
#     for row in time_ma[tiem_]:
#         print(*row)
# 8초 지났으면 return true
drdc = list(product([-1,0,1], [-1,0,1]))
inrange = lambda  r, c : bool(0<=r<8 and 0<=c<8)

def bfs():
    time_ = 0
    q = deque()
    q.append((7,0))
    vset = set()
    vset.add((7,0,0)) # r, c, time
    while q:
        if time_ > 8:
            return 1
        for _ in range(len(q)):
            cr, cc = q.popleft()

            if time_ma[time_][cr][cc] == "#":
                continue #이동불가

            if cr == 0 and cc == 7:
                return 1

            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc
                if not inrange(nr,nc):
                    continue
                if time_ma[time_][nr][nc] == "#":
                    continue
                nxt = (nr,nc,time_+1)
                if nxt in vset:
                    continue
                q.append((nr,nc))
                vset.add(nxt)
        time_ += 1
    return 0

print(bfs())
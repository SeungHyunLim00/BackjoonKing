# 레드스톤
# B 는 16으로 시작한다 -> 논리 오류가 없나??
# 09:28 예제 다맞 ->
# 1차 제출 실패
# 아 "모든 레드 스톤 램프가 켜지는 순간이 있는지"
# => 시간순으로 묶어야 하는 거였음. 지금은 시간에 관계 없이
# => 시간순으로 묶어서 다 겹치는 곳 있나 봐야함
# 어차피 최대가 16이니까 그냥 table 만들어서 더하기로
# 걸리는 부분
# 1. 시간에 대한 이해 -> D가 어차피 다 오는데
# 오는 시간 = 16 - ce
# 아니 어차피 B가 계속 공급해주는데 그냥 모두 도달 가능하면 되는거 아님??

DEBUG = False
from collections import deque

drdc = [(1,0), (-1,0), (0,1), (0,-1)]
W, H = map(int, input().split())
N = int(input())

matrix = [["."]*H for _ in range(W)]
elec = [[0]*H for _ in range(W)]


tot_lamp = 0
q = deque()

for _ in range(N):
    type, r, c = input().split()
    r, c = int(r), int(c)
    if type == "redstone_dust":
        matrix[r][c] = "D"
    elif type == "redstone_block":
        matrix[r][c] = "B"
        elec[r][c] = 15
        q.append((r, c, 16))
    else:
        tot_lamp += 1
        matrix[r][c] = "L"

def solve():
    visit_lamp = set()
    time_ = 0
    while q:
        for _ in range(len(q)):
            cr, cc, ce = q.popleft()

            if matrix[cr][cc] == "L":
                visit_lamp.add((cr, cc))
                continue

            if ce == 1: continue
            ne = ce - 1

            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc

                if not (0<=nr<W and 0<=nc < H): continue
                val = matrix[nr][nc]
                if val == "." or val == "B": continue
                if elec[nr][nc] >= ne: continue
                q.append((nr,nc, ne))
                elec[nr][nc] = ne
        time_ += 1

    if len(visit_lamp) == tot_lamp:  # 이거 잘 되나?
        return True
    else:
        return False

print("success") if solve() else print("failed")
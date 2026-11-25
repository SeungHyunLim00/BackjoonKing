# 캐슬 디펜스
# 구상 5분
# 시복 : 15(turn) x (15C3 x 3x D(10) ~= 27000 충분
# 그거 뭐냐 피곤한 귀가길과는 다르게
# 같은 N이라서 아 아니다 여기도 퍼져가는거 신경
# 같은 visited를 공유해도 되는가
# clear 시점 -> 발견 했을때만 하면 ㄴㄴ 미발견시 v가 초기화 안돼서 방문x
# 아예 matrix를 내려버리는데 그게 반복되니까 시간(M)만큼 저장할 수도 있음
# 근데 귀찮다

from itertools import combinations
from collections import deque

DEBUG = False
def myprint(string, pick):
    if not DEBUG: return
    print(f"-------{string}---------")
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if (r, c) in pick:
                print(f"A", end =" ")
            else:
                print(f"{val}", end = " ")
        print()

drdc = [(0,-1),(-1,0), (0,1)] # 왼쪽이 가장

N, M, D = map(int, input().split())

tot_enemy = 0
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
    for val in matrix[-1]:
        if val == 1: tot_enemy += 1
matrix.append([2]*M)

orig = [lst[:] for lst in matrix]

coords = [(N, i) for i in range(M)]

ans = 0
q = deque()
v = set()
attack = set()
cnt = 0
for pick in combinations(coords, 3):
    cnt += 1
    dead = 0
    finish = 0
    q.clear()
    matrix = [lst[:] for lst in orig ]

    myprint("start pick", pick)

    while True: # turn당
        attack.clear()

        for r, c in pick:
            v.clear(); q.clear()
            q.append((r,c,D))
            v.add((r,c))
            found = False
            while q:
                for _ in range(len(q)):
                    cr, cc, d = q.popleft()

                    if matrix[cr][cc] == 1:
                        #print(f"archer {r,c} choose {cr, cc}")
                        found = True
                        attack.add((cr,cc))
                        break
                    if d == 0: continue
                    for dr, dc in drdc:
                        nr, nc = cr + dr, cc + dc
                        if not (0<=nr<N and 0<=nc<M): continue
                        if (nr,nc) in v: continue
                        v.add((nr,nc))
                        q.append((nr,nc, d - 1))
                if found: break

        for r, c in attack:
            matrix[r][c] = 0
            dead += 1
            finish += 1
        if finish == tot_enemy : break

        myprint("aft attack", pick)
        # 적 이동
        move = []
        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 1:
                    move.append((r+1, c))
                    matrix[r][c] = 0

        for r, c in move:
            if matrix[r][c] == 2:
                finish += 1
            else:
                matrix[r][c] = 1

        myprint("aft move", pick)
        if finish == tot_enemy: break


    ans = max(dead, ans)


print(ans)
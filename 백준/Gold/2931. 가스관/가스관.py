# 가스관
# 19:03 ~ 19:33 구상 30분
# 모스크바와 자그레브가 하나의 블록과 인접해있는 입력만
# 아놔 이거때문에 한참 고민했는데 문제나 한번 더 읽을걸
# 19:49 예제 2번에서 M옆에 - 이거 인데 그냥 옆에 파이프가 있단 이유로 + 해버림

# 19:53 예제 다맞 검증 시작
# 아 검증하기 귀찮아
# 20:00 1차 제출 실패 -> 왤까..
# 의심가는 곳 : 빈칸채우기 로직 - 다시 생각해보자
# 아 그거때문이네

DEBUG = False
from collections import deque

R, C = map(int, input().split())

drdc = [(0,-1), (-1,0), (0,1), (1,0)]
pipes = {
    '|':{1:1, 3:3},
    '-':{0:0, 2:2},
    '+':{0:0,1:1,2:2,3:3},
    '1':{0:3, 1:2},
    '2':{0:1,3:2},
    '3':{2:1,3:0},
    '4':{1:0, 2:3}
}

sr, sc = -1, -1
er, ec = -1, -1

matrix = []
for r in range(R):
    matrix.append(list(input().strip()))
    for c, val in enumerate(matrix[-1]):
        if val == "M":
            sr, sc = r, c
        elif val == "Z":
            er, ec = r, c

sd = -1
for d, (dr, dc) in enumerate(drdc): # 시작 dir 정하기
    nr, nc = sr + dr, sc + dc
    if not (0<=nr<R and 0<=nc<C) : continue
    nval = matrix[nr][nc]
    if nval != "." :
        if nval in pipes:
            sd = d; break

print(f"start {sr, sc, sd}") if DEBUG else 0

q = deque()
q.append((sr, sc, sd))

empty = None
e_in, e_out = -1, -1
ans = None

while q:
    cr, cc, cd = q.popleft()
    print(f"im here {cr, cc, cd}") if DEBUG else 0
    if cd != -1:
        if cr == sr and cc == sc: outd = cd
        else:
            p = matrix[cr][cc] #어떤 파이프
            outd = pipes[p][cd]
            print(f"at pipe {p} in {cd} -> {outd}") if DEBUG else 0

        dr, dc = drdc[outd]
        nr, nc = cr + dr, cc + dc
        if matrix[nr][nc] == ".":# 빈칸임 -> 채워야할 곳
            empty = (nr, nc)
            q.append((nr,nc, -1))
            e_in = outd
        else:
            q.append((nr, nc, outd))

    else: # 여기가 채워야할 곳임 ( 빈칸있는 matrix)
        cnt = 0
        for d, (dr, dc) in enumerate(drdc):
            if d == (e_in + 2)% 4 : continue # 다시 돌아가는 방향은 ㄴㄴ
            nr, nc = cr + dr, cc + dc
            if not (0<=nr<R and 0<=nc<C): continue

            p = matrix[nr][nc]
            if p in (".", "M", "Z") : continue
            if d in pipes[p]: # 그 방향을 받아들이는 때만
                cnt += 1
                e_out = d

        print(f"empty {empty} : {e_in} => {e_out} ") if DEBUG else 0

        if cnt != 1:
            ans = "+"
        else:
            for p, p_dict in pipes.items():
                if p == "+": continue
                for in_, out_ in p_dict.items():
                    if in_ == e_in and out_ == e_out:
                        ans = p
                        break
                if ans is not None: break
        break

print(empty[0]+1, empty[1]+1, ans)
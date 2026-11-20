# 상범빌딩
# 구상 4분 ~ 13:19
# 구현 15분
# 1차 성공
from collections import deque

dhdrdc = [(-1,0,0),(1,0,0),(0,-1,0),(0,0,1),(0,1,0),(0,0,-1)]
#           상       하       북       동   남       서

def bfs():
    # 30**3 이니까 27000  -> 흐으으음 귀찮다 set으로 하자
    vset = set()
    q = deque()
    q.append((sh, sr, sc))
    vset.add((sh, sr, sc))
    dist = 0
    while q:
        for _ in range(len(q)):
            ch, cr, cc = q.popleft()
            if ch == eh and cr == er and cc == ec:
                return dist
            for dh, dr, dc in dhdrdc:
                nh, nr, nc = ch + dh, cr + dr, cc + dc
                if not(0<=nh<L and 0<=nr<R and 0<=nc<C):
                    continue
                if building[nh][nr][nc] == "#":
                    continue
                nxt = (nh, nr, nc)
                if nxt in vset:
                    continue
                q.append(nxt)
                vset.add(nxt)
        dist += 1
    return -1

while True:
    cmd = list(map(int, input().split()))
    if cmd == [0,0,0]:
        break

    L, R, C = cmd
    sh, sr, sc = -1, -1, -1
    eh, er, ec = -1, -1, -1

    building = []
    for h in range(L):
        matrix = []
        for r in range(R):
            matrix.append(list(input().strip()))
            for c, val in enumerate(matrix[-1]):
                if val == "S":
                    sh, sr, sc = h, r, c
                elif val == "E":
                    eh, er, ec = h, r, c
        input()
        building.append(matrix)

    # print(f"{sh,sr,sc} -> {eh, er, ec}")
    # for h in range(L):
    #     print(f"======floor{h}=====")
    #     for row in building[h]:
    #         print(*row)

    ans = bfs()

    if ans == -1:
        print(f"Trapped!")
    else:
        print(f"Escaped in {bfs()} minute(s).")
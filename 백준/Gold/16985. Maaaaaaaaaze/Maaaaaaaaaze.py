#Maaaaaaaaaze
# 19:09 ~ 19: 13 구상
# 시복 계산 4**5 x 5! -> 10**4 정도 ㄱㅊ
# 어차피 회전을 4방향 다 하기에 시작, 출구는 000, 444로 고정
# minor debug: bfs에서 방문 못할 시에 답(INF)처리 -> 맨날뺴먹음
# 범위실수 -> <4로 기입
# 19:42 : 예제 4 오답나옴 22 -> 12
# wow 0: 못감 -> 1 감 이거 반대로
from collections import deque
from itertools import permutations, product


INF = int(1e9)
dhs = [0, 0, 0, 0, 1, -1]
drs = [1, -1, 0, 0, 0, 0]
dcs = [0, 0, 1, -1, 0, 0]

ROTATES_PANS = [] # 각 판 번호 -> rot 이동

for _ in range(5):
    one_pan = []
    for _ in range(5):
        one_pan.append(list(map(int, input().split())))
    # 이건 original pan이다.

    ROTATES_PANS.append([one_pan[:]]) # 0번째
    for rot_num in range(4):
        one_pan = [list(lst) for lst in zip(*one_pan[::-1])]
        ROTATES_PANS[-1].append(one_pan[:])

# check = ROTATES_PANS[4][3]
# for row in check:
#     print(*row)
#
# exit()

def bfs(trans):
    global answer

    def react(h, r, c):
        realh, rot = trans[h]
        return ROTATES_PANS[realh][rot][r][c]

    q = deque()
    if react(0,0,0) == 0: return INF
    q.append((0,0,0))

    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True

    dist = 0
    while q:
        for _ in range(len(q)):
            ch, cr, cc = q.popleft()
            if ch == 4 and cr == 4 and cc == 4:
                return dist

            for dh, dr, dc in zip(dhs, drs, dcs):
                nh, nr, nc = ch + dh, cr + dr, cc + dc
                if not (0<=nh<5 and 0<=nr<5 and 0<=nc<5): continue
                if visited[nh][nr][nc] : continue
                if react(nh, nr, nc) == 0 : continue
                q.append((nh, nr, nc))
                visited[nh][nr][nc] = True
        dist += 1
        if dist >= answer: return INF
    return INF


answer = INF
for h0, h1, h2, h3, h4 in permutations([0,1,2,3,4]):


    for r0,r1,r2,r3,r4 in product([0,1,2,3], repeat = 5):
        trans = {0: (h0, r0), 1: (h1,r1), 2: (h2,r2), 3: (h3,r3), 4: (h4, r4)}
        #print(trans)
        answer = min(bfs(trans), answer)


print(answer) if answer != INF else print(-1)
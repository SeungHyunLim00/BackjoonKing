# 새벽의 탐정게임
# 09:00 ~ 09:13 구상
# 09:26 예제 3 다 맞음

from collections import deque

# 구상 : 0~ 5까지 각
#   0   1    2   3    4    5
# 아래  위  앞   좌  뒤    우

drdc = [(1,0), (0,-1), (-1,0), (0,1)]

def roll_dice(num, d):# 현재 빈칸이 있는 칸, 회전시킬 방향
    if d == 0:
        trans = {0:4, 1:2, 2:0, 4:1, 3:3, 5:5}
    elif d == 1:
        trans = {0:5, 3:0, 1:3, 5:1, 2:2, 4:4}
    elif d == 2:
        trans = {0:2, 2:1, 4:0, 1:4,3:3, 5:5}
    elif d == 3:
        trans = {5:0, 1:5, 3:1, 0:3, 2:2, 4:4}
    return trans[num]

N, M = map(int, input().split())
matrix = []
sr, sc = -1, -1
for r in range(N):
    matrix.append(input())# list로 안받고 그냥 하겠다
    for c, val in enumerate(matrix[-1]):
        if val == "D":
            sr, sc = r, c

q = deque()
q.append((sr, sc, 0))

visited = [[0]*M for _ in range(N)]
visited[sr][sc] |= 0<<1
dist = 0
success = False
while q:

    for _ in range(len(q)):
        cr, cc, state = q.popleft()

        if matrix[cr][cc] == "R":
            if state == 0:
                success = True
                break
            continue # 아니면 탐정이 진것.-> 더이상 진행x
        for d, (dr, dc) in enumerate(drdc):
            nr, nc = cr + dr, cc + dc
            if matrix[nr][nc] == "#": continue # padding
            # 도둑 및, 출발지점 갈 수 있기에 R, D도 갈 수 있어야함
            n_state = roll_dice(state, d)
            if visited[nr][nc] & 1<<n_state: continue
            q.append((nr,nc, n_state))
            visited[nr][nc] |= 1<< n_state

    if success: break
    dist += 1

print(dist) if success else print(-1)
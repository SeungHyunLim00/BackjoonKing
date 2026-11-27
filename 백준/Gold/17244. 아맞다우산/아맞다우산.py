# 아맞다 우산
# 5개 이하면 bit고,
# 상태관리 bfs랑 다르려나? 무식하게 바로 구현 가보자
# 구상 2분
# 11:43 구현시작
# 마이너디버깅 : 또 종료조건에 return 하고 아닐때는 지속할뻔

from collections import deque

drdc = [(1,0), (-1,0), (0,1), (0,-1)]
ob_idx = 0
ob_dict = dict()

sr, sc = -1, -1
M, N = map(int, input().split()) # 누가 세로를 M으로 줌 미친문제
matrix = []

for r in range(N):
    matrix.append(input()) # 바꾸는게 없으므로 string그대로 받겠다
    for c, val in enumerate(matrix[-1]): #
        if val == "X":
            ob_dict[(r,c)] = ob_idx
            ob_idx += 1
        elif val == "S":
            sr, sc = r, c

# print(sr, sc)
# print(ob_dict)
# print(ob_idx)
def solve():
    q = deque()
    q.append((sr, sc, 0)) # state, 아무것도 없음 =

    visited = [[0]*M for _ in range(N)]
    visited[sr][sc] |= 1<<0 # 얘는 1~ 32까지 하는애임

    dist = 0

    while q:
        for _ in range(len(q)):
            cr, cc, state = q.popleft()
            #print(f"{cr, cc} : {bin(state)[2:]}")
            if matrix[cr][cc] == "E":
                if state == 2**(ob_idx)-1 :
                    return dist
                else:
                    continue

            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc
                nstate = state
                if matrix[nr][nc] == "#": continue # 패딩덕에 범위x
                if matrix[nr][nc] == "X":
                    nstate |= (1<<ob_dict[(nr,nc)])

                if visited[nr][nc] & 1<<nstate: continue

                q.append((nr, nc, nstate))
                visited[nr][nc] |= (1<<nstate) # 여기 그냥 nstate으로 해버려서

        dist += 1

    return -1

print(solve())
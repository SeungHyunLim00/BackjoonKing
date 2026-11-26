# Maze in Bolt
# 16:40 ~ 16:48 독해(영어...?)
# 아니 한줄인데 flip은 왜 넣는거?
# 디버깅 5분 : 괜히 str로 받았다 다 true
# 아니 bfs로 해야지
# 아니 이거 위로도 갈 수 ㅣㅇㅆ는거잖아 심지어 어린왕자

from collections import deque
drdc = [(1,0), (0,1), (-1,0), (0,-1)]
R, C = map(int, input().split())

nuts = list(map(int, input().strip()))
bolox = [idx for idx in range(C) if nuts[idx]]

bolts = []
for _ in range(R):
    bolts.append(list(map(int, input().strip())))

def okay(cr, cc):
    for c in range(C):
        if bolts[cr][c] and nuts[(cc + c) % C]:
            return False
    return True

def solve():
    q = deque()
    visited = [[False]*C for _ in range(R)]
    for c in range(C):
        q.append((0, c))
        visited[0][c] = True

    while q:
        cr, cc = q.popleft()
        if cr == R:
            return True

        if not okay(cr, cc): continue

        for dr, dc in drdc:
            nr, nc = cr + dr, cc + dc
            if not (0<=nr<=R): continue
            if not(0<=nc<C):
                nc = nc % C
            # 범위주의
            if nr == R: return True
            if visited[nr][nc] : continue
            q.append((nr, nc))
            visited[nr][nc] = True


if solve():
    print("Y")
else:
    nuts = nuts[::-1]
    print("Y") if solve() else print("N")
# 뿌요뿌요
#그럼 터질 게 여러개면?? -> 한번에 없어진다
# 익숙한 중력 + bfs라 바로 구현 ㄱ
# 11:20 구현 시작
from collections import deque

DEBUG = False

def myprint(string):
    if not DEBUG : return
    print(f"======{string}======")
    for row in matrix:
        print(*row)

drdc = [(1,0), (-1,0), (0,1), (0,-1)]
trans = {".":0, "R":1, "G":2, "B":3, "P":4, "Y":5}
matrix = []
for _ in range(12):
    matrix.append(list(map(lambda t : trans[t], input().strip())))

def pang():
    q = deque()
    visited = [[False]*6 for _ in range(12)]
    temp  = []
    did = False
    for r in range(12):
        for c in range(6):
            if visited[r][c] or matrix[r][c] == 0 : continue
            temp.clear()
            val = matrix[r][c]
            q.append((r, c))
            visited[r][c] = True
            while q:
                cr, cc = q.popleft()
                temp.append((cr, cc))
                for dr, dc in drdc:
                    nr, nc = cr + dr, cc + dc
                    if not (0<=nr<12 and 0<=nc<6) : continue
                    if visited[nr][nc] : continue
                    if matrix[nr][nc] == 0: continue
                    if matrix[nr][nc] == val :
                        q.append((nr,nc))
                        visited[nr][nc] = True
            if len(temp) >= 4:
                did = True
                for tr, tc in temp:
                    matrix[tr][tc] = 0
    return did

def gravity():

    for c in range(6):
        ep = 11
        for r in range(11, -1, -1):
            if matrix[r][c]:
                if ep != r:
                    matrix[r][c], matrix[ep][c] = matrix[ep][c], matrix[r][c]
                ep -= 1
cnt = 0
while True:
    if pang():
        myprint(f"after {cnt+1}th pang")
        gravity()
        myprint(f"after gravity")
        cnt += 1
    else: break

print(cnt)
#상남자
# 19:05 ~ 19:23 구상 18분
# 처음에는 l, r 남은거 q 안에 넣으려다 MxM 조합 생각하면 v 터짐.
# 좌표에 갔을 때 최소 로 관리
# 1000x1000 case 만들어보기
# 19:36 구상 헛점 발견. c로만 하면 완됨...올때까지 최소 그거 저장
# 아 for문 아니고 그냥 L,R해서 continue 하면 안돼 ㅠㅠ
# 조건 반대로 안써서 함 틀리고 -> 3분만에 맞음
# 19:44 예제 맞, 검증 ㄱㄱ
# 19:50 1000x1000 케이스에서 ㄱㅊ은듯
# 1차 제출 실패 - 생각을 해보자
# 아 거리가 최단이지 왼오가 최단은 아니구나



from collections import deque


N, M = map(int, input().split())
L, R = map(int, input().split())

sr, sc = -1, -1
matrix = []
for r in range(N):
    matrix.append(input()) # 바뀌는게 없으므로 string으로 받아줌
    for c, val in enumerate(matrix[-1]):
        if val == "2":
            sr, sc = r, c

q = deque()
q.append((sr, sc))
visited = [[None]*M for _ in range(N)]
visited[sr][sc] = (0,0)


drdc = [ (-1,0), (1,0)]



comp = lambda r, c : sum(visited[r][c])

while q:
    cr, cc = q.popleft()
    usedl, usedr = visited[cr][cc]
    #print(f"cr, cc {cr, cc} with {usedl, usedr}")
    # 왼쪽:
    if usedl != L:
        nr, nc = cr, cc - 1
        if (0 <= nr < N and 0 <= nc < M) and\
            matrix[nr][nc] != "1":
            if not visited[nr][nc] or comp(nr,nc) > comp(cr, cc) + 1:
                q.append((nr,nc))
                visited[nr][nc] = (usedl + 1, usedr)
    if usedr != R:
        nr, nc = cr, cc + 1
        if (0 <= nr < N and 0 <= nc < M) and \
                matrix[nr][nc] != "1":
            if not visited[nr][nc] or comp(nr, nc) > comp(cr, cc) + 1:
                q.append((nr,nc))
                visited[nr][nc] = (usedl, usedr+1)

    for dr in (-1, 1):
        nr, nc = cr + dr, cc
        if not (0<=nr<N and 0<=nc<M): continue
        if matrix[nr][nc] == "1": continue

        if not visited[nr][nc] or comp(nr, nc) > comp(cr, cc) :
            q.append((nr,nc))
            visited[nr][nc] = (usedl, usedr)

# for r, row in enumerate(visited):
#     for c, val in enumerate(row):
#         if val:
#             l, r = val
#             print(f"{l}|{r}", end = " ")
#         else:
#             if matrix[r][c] == "1": print("BBB",end=" ")
#             else: print("   ",end=" ")
#     print()


print(sum(sum(1 if val else 0 for val in row ) for row in visited))
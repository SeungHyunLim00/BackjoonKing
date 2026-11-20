# 배달
# 구상 10분 ( 뭔가 놓친 것 같은데 내 뇌로는 쉬운 문제임)
# 구현 0922 ~
# 하다가 생각 아, visited 관리가 tricky 하구나. 이전 방향 기준으로 해야겠다.
# 구현 디버깅내용
#   pastd 인데 usedd 잘못씀
#   typo : sr_, sc_ 인데 sr, sc 씀
# bfs/dfs 시에 디버깅(지나온 track 가시화) 잘하는 법 없을까?
# 10:05 구현 완료
# 검증 제대로 안했지
# -> 벽도 안보고, -1 조건도 빠트림
# edge
# 1 x 1일때 -> 불가
# 2차 제출 10:09 통과
# 11:20 다시풀기 : 놀랍게도 bfs를 나누면 안됨. -> 가능한 도착 방향 다 넘겨줘야

from collections import deque

DEBUG = False
# Step1 기초공사
INF = int(1e9)
drdc = [(0,-1), (-1,0), (0,1), (1,0)]
#       좌       상       우       하
trans = lambda x : chr(0x2190 + x)
inrange = lambda r, c : bool(0<=r<N and 0<=c<M)
# padding 할까 하다 그냥...

N, M = map(int, input().split()) # 1~50

sr, sc, cr1, cc1, cr2, cc2 = -1,-1,-1,-1,-1,-1
matrix = []
for r in range(N):
    matrix.append(list(input().strip()))
    for c, val in enumerate(matrix[-1]):
        if val == "S":
            sr, sc = r, c
            matrix[sr][sc] = "." # 이동을 위해 좌표만 저장
        elif val == "C":
            if cr1 == -1:
                cr1, cc1 = r, c
            else:
                cr2, cc2 = r, c
            matrix[r][c] = "." # 이것도 좌표로만

# 확인
if DEBUG:
    for row in matrix:
        print(*row)
    print(f"start at {sr, sc}")
    print(f"C1 : {cr1, cc1}")
    print(f"C2 : {cr2, cc2}")


def bfs(sr_, sc_, er, ec, used_d):

    visited = [[[False, False, False, False] for _ in range(M)] for _ in range(N)]

    q = deque()
    for d in used_d:
        q.append((sr_, sc_, d)) # 이전에 방문했던 방향별로
        visited[sr_][sc_][d] = True
    # 각 칸에 '들어온' 방향 기준. 따라서 시작점은 없음.

    dist = 0

    arrive_d = []
    while q:

        for _ in range(len(q)):
            cr, cc, pastd = q.popleft()
            #print(f"at {dist} : {cr, cc} with {trans(pastd)}")

            if cr == er and cc == ec:
                arrive_d.append(pastd)
                continue

            for d, (dr, dc) in enumerate(drdc):
                if d == pastd:
                    continue
                nr, nc = cr + dr, cc + dc
                if not inrange(nr,nc):
                    continue
                if visited[nr][nc][d]:
                    continue
                if matrix[nr][nc] == "#":
                    continue
                q.append((nr,nc,d))
                visited[nr][nc][d] = True
        if arrive_d:
            return dist, arrive_d
        dist += 1

    return -1, arrive_d

# C1->C2 case

time1, usedd = bfs(sr, sc, cr1, cc1, [-1]) # 처음은 used가 없음
print(f"arrive c1 {time1} with {usedd}") if DEBUG else 0
time2, check = bfs(cr1, cc1, cr2, cc2, usedd)
print(f"arrive c2 {time2} with {check}") if DEBUG else 0

if not usedd or not check:
    res1 = -INF
else:
    res1 = time1 + time2

# C2 -> C1 case
print(f"====Case 2====") if DEBUG else 0
time3, usedd = bfs(sr, sc, cr2, cc2, [-1]) # 처음은 used가 없음
time4, check = bfs(cr2, cc2, cr1, cc1, usedd)
print(f"arrive c2 {time3} with {usedd}") if DEBUG else 0
print(f"arrive c1 {time4} with {check}") if DEBUG else 0
if not usedd or not check:
    res2 = -INF
else:
    res2 = time3 + time4
print(f"here {res1} {res2} ") if DEBUG else 0

result = min(res1, res2)
if result == -INF:
    print(-1)
else:
    print(result)
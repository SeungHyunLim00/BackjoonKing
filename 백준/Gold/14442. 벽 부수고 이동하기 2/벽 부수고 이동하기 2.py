# 벽 부수고 이동하기
# 구상 19:18 ~19:19
# 그냥 벽 뚫은 갯수 추가해주면 될 줄 알았는데, 어떤 곳에 최단으로 가더라도
# 벽을 너무 많이 뚫으면 소용이 없자너
# visited 관리를 다르게 해야할듯 10^6이다
# -> K가 다행히 10 이하이므로 3차원으로 하자 -> 아니다 에라이 비트로 하자
# 1차이가 남
# 디버깅
# 1. 일단 visited 찍기 -> bit 첨 가시화해봄. 2: 해서 보는거
# 2. 문제 다시 읽기 -> 아 첫 칸 포함이구나
# 19:38 구현완료

drdc = [(1,0), (-1,0), (0,1), (0,-1)]

from collections import deque
N, M, K = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().strip())))

sr, sc = 0,0
er, ec = N-1, M-1

visited = [[0]*M for _ in range(N)]
q = deque()
q.append((sr, sc, 0)) # 마지막은 뚫은 벽 수
visited[sr][sc] = 2**10 - 1 # start를 다시 방문할 일은 없다.

ans = -1
dist = 0

while q:
    dist += 1 # 시작칸과 끝 칸을 포함해서 센다
    for _ in range(len(q)):
        cr, cc, destroy = q.popleft()

        if cr == er and cc == ec:
            ans = dist
            break
        nxtd = destroy + 1
        for dr, dc in drdc:
            nr, nc = cr + dr, cc + dc
            if not (0<=nr<N and 0<=nc<M):
                continue
            if matrix[nr][nc] == 1:
                if destroy == K or visited[nr][nc] & 1<<nxtd:
                    continue
                q.append((nr, nc, nxtd))
                visited[nr][nc] |= 1 << nxtd
            else:
                if visited[nr][nc] & 1 << destroy:
                    continue
                q.append((nr, nc, destroy))
                visited[nr][nc] |= 1 << destroy


    if ans != -1:
        break

print(ans)

# for row in visited:
#     for val in row:
#         print(f"{bin(val)[2:]:10s}", end = " ")
#     print()
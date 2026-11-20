# 녹색 옷 입은 애가
# 09:00 ~ 09:03 독해
# 09:11 1차제출 성공
from heapq import heappush, heappop

INF = int(1e9)
drdc = [(1,0), (-1,0), (0,1), (0,-1)]
inrange = lambda r, c : bool(0<=r<N and 0<=c<N)

prob = 1
while True:
    N = int(input())
    if N == 0:
        break
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    visited = [[INF]*N for _ in range(N)]
    visited[0][0] = matrix[0][0]
    hq = [(matrix[0][0], 0,0)] # val, r, c
    while hq:
        cost, cr, cc = heappop(hq)

        if cr == N-1 and cc == N-1: # 이거 확인
            break
        # 여기서 가지치기 들어가야함??
        # cost >= visited[cr][cc]? 그럼 0번째에 짤 되고...

        for dr, dc in drdc:
            nr, nc = cr + dr, cc + dc

            if not inrange(nr,nc):
                continue
            ncost = cost + matrix[nr][nc]
            if visited[nr][nc] <= ncost:
                continue
            heappush(hq, (ncost, nr, nc))
            visited[nr][nc] = ncost
    print(f"Problem {prob}: {visited[N-1][N-1]}")
    prob += 1
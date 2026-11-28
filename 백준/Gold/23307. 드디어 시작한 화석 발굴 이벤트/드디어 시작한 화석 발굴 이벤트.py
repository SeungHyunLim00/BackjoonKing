#드디어 시작한 화석발굴

# NxN크기 -> 오염물질
# 달팽이다!!
# 아니 그냥 floodfill 하고 방향만 신경쓰면 되는거 아님? start 지점이랑 end 지점
# 그게 어렵군 훔.....끝 : 빈칸 3개
# 안쪽 바깥쪽 : 안쪽이 무조건 나중에 도달함 -> 아닌데??
# 아 신경쓸 필요가 없다 -> 아니다 신경 써야함
#아니3ㄱ389837 행작열작

from collections import deque
N = int(input())
drdc = [(1,0), (0,1),(-1,0), (0,-1)]

matrix = []
for _ in range(N):
    matrix.append(input())

def panbyeol(outer, inner):
    d1, r1, c1 = outer
    d2, r2, c2 = inner
    if d1==2: # U
        if c1 < c2 : return "UL"
        else: return "UR"
    elif d1 == 3:
        if r1 < r2 : return "LU"
        else: return "LD"
    elif d1 == 1:
        if r1 < r2 : return "RU"
        else: return "RD"
    else:
        if c1 < c2: return "DL"
        else: return "DR"


ans = []

visited = [[0]*N for _ in range(N)]

q = deque()
gnum = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] : continue
        if matrix[r][c] == ".": continue

        gnum += 1
        temp = []
        q.append((r,c))
        visited[r][c] = gnum

        while q:

            cr, cc = q.popleft()
            cnt = 0
            ed = -1
            for d, (dr, dc) in enumerate(drdc):
                nr, nc = cr + dr, cc + dc
                if not (0<=nr<N and 0<=nc<N): cnt += 1; continue
                if matrix[nr][nc] == ".": cnt += 1; continue
                ed = d
                if visited[nr][nc] : continue
                q.append((nr, nc))
                visited[nr][nc] = gnum

            if cnt == 3:
                temp.append(((ed + 2)%4, cr, cc))

        outer, inner = None, None
        for cd, cr, cc in temp:
            dr, dc = drdc[cd]
            nr, nc = cr + 2*dr, cc + 2*dc
            if (0 <= nr < N and 0 <= nc < N) and visited[nr][nc] == gnum:
                inner = (cd, cr, cc)
            else:
                outer = (cd, cr, cc)

        length = (abs(outer[1] - inner[1]))*2 + 1
        #print(outer[1]-inner[1])
        ans.append((inner[1]+1, inner[2]+1, length, panbyeol(outer, inner)))

print(len(ans))
ans.sort()
for a in ans:
    print(" ".join(map(str,a)))




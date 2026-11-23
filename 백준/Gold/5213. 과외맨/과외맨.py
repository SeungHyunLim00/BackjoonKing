# 과외맨
# 구상 19:10 ~ 19:20
# input좀 잘 받고, 도착지 달라지는거 주의
# 500x500이라 matrix 가능
# 아 drdc 다 넣지말고 2방향만 해도...? 에이 몰라 걍 해봐
# 아니다 s자 모양으로 꺾어질 수도 있구나
# 마이너 디버깅 : tracks 안넣을 때 continue 해서 무한뤂 걸림
# inrange 범위 및 visited 범위
# 19:56 다 맞음. 예제 2번은 dr dc때문에 다르게 나오는듯
# 아니 다르게 나올 수도 있으면 그것도 알려줘야지
# 검증 ㄱ
# 검증때 발견 : 마지막 줄의 마지막 타일로 이동할 수 없는 경우가 존재할 수 있다. 이 경우에는 번호가 가장 큰 타일로 이동하면 된다.
# 마지막 케이스 => 어떻게 잘 해결했네....? # 어케 알지
# 아니 이거 검증 안해도 되나? 내가 알아서 처리한건가?
# 일단 찜찜해서 arrival 안했을때 역순으로 타고 올라가는거 처리함
# 20:06 1차 제출 -> 런타임에러 : index 에러인가?
# 20:08 2차 제출 실패 흠..
# 경로의 길이(bfs) 가 짧아도 타일은 길 수가 있나??
# q 난리쳤다가 밀고 그냥 dict로
from collections import deque

INF = int(1e9)
drdc = [(1,0), (0,1), (-1,0), (0,-1)]
N = int(input())
inrange= lambda r, c : bool(0<=r<N and 0<=c<2*N)

matrix = []
nums = []
idx = 1
for r in range(N):
    matrix.append([])
    nums.append([])
    if r % 2 == 0:
        for c in range(0, 2*N, 2):
            matrix[-1].extend(list(map(int, input().split())))
            nums[-1].extend([idx]*2)
            idx += 1
    else:
        matrix[-1].append(0)
        nums[-1].append(0)
        for c in range(0, 2*N-2, 2):
            matrix[-1].extend(list(map(int, input().split())))
            nums[-1].extend([idx]*2)
            idx += 1
        matrix[-1].append(0)
        nums[-1].append(0)

# for row in matrix:
#     print(*row)
# print(f"==================")
# for row in nums:
#     for val in row:
#         print(f"{val:2d}", end = ' ')
#     print()

def finish(r, c):
    if N%2 == 0:
        if r == N-1 and (c == 2*(N-2)+1 or c == 2*(N-2) + 2): return True
    else:
        if r == N-1 and c == 2*(N-1) : return True
    return False

q = deque()
q.append((0,0))
q.append((0,1))
visit = dict()
visit[1] = 0

arrival = False


def other(r, c): # 나머지 반
    if c + 1 < 2*N and nums[r][c+1] == nums[r][c]: return c + 1
    return c - 1

while q:
    cr, cc = q.popleft()
    tile = nums[cr][cc]

    if finish(cr, cc):
        arrival = True
        break

    for d, (dr, dc) in enumerate(drdc):
        nr, nc = cr + dr, cc + dc

        if not inrange(nr,nc) : continue

        if matrix[nr][nc] == 0 : continue
        ntile = nums[nr][nc]
        if ntile == 0 : continue
        if ntile in visit:continue

        if matrix[nr][nc] != matrix[cr][cc] : continue
        q.append((nr,nc))
        q.append((nr, other(nr, nc)))
        visit[ntile] = tile


# print(f"finish")
# for row in visited:
#     for val in row:
#         if val is None:
#             print(f"XXX", end=" ")
#         else:
#             print(f"{val[0]} {val[1]}", end=" ")
#     print()

if not arrival:
    end = -1
    for r in range(N-1, -1, -1):
        for c in range(2*N-1, -1, -1): # 역순
            num = nums[r][c]
            if num == 0 : continue
            if num in visit:
                end = num
                break
        if end != -1: break

    #print(f"heree {cr, cc} and {nums[cr][cc]}")
else:

    end = idx - 1 # 마지막 타일

tracks = []
while end != 0:
    tracks.append(end)
    end = visit[end]

print(len(tracks))
print(*tracks[::-1])
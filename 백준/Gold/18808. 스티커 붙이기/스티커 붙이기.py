# 스티커 붙이기
# 구상 10분
# 예제 다맞 -> 10:14
# 귀찮다 검증 해야할까


def rotate(r, c): return c, -r

def get_coord(R, C, temp_):

    coords = []

    sr, sc = -1, -1
    for r in range(R):
        for c in range(C):
            if temp_[r][c]:
                if sr == -1:
                    sr, sc = r, c
                coords.append((r-sr, c- sc))
    return coords



N, M, K = map(int, input().split())

STICKERS = [] # i번째 -> 0, 1, 2,3 번 돌려진 것들
for st in range(K):
    STICKERS.append([])
    R, C = map(int, input().split())
    temp = []
    for _ in range(R):
        temp.append(list(map(int, input().split())))

    coord = get_coord(R, C, temp)
    STICKERS[-1].append(coord[:])
    for _ in range(3):
        aft_coord = []
        for r, c in coord:
            aft_coord.append(rotate(r, c))
        #print(f"for st{st} rot num : {aft_coord}")
        coord = aft_coord
        STICKERS[-1].append(coord[:])

matrix = [[0]*M for _ in range(N)]
for st_num in range(K):
    sucess = None

    for rot_num in range(4):
        for sr in range(N):
            for sc in range(M):
                for rr, rc in STICKERS[st_num][rot_num]:
                    nr, nc = sr + rr, sc + rc
                    if not(0<= nr <N and 0<= nc <M): break
                    if matrix[nr][nc] : break
                else:
                    sucess = (sr, sc, rot_num); break
            if sucess: break
        if sucess: break

    if sucess:
        sr, sc, rot_num = sucess
        for rr, rc in STICKERS[st_num][rot_num]:
            matrix[sr + rr][sc + rc] = 1

    # print(f"===aft {st_num}======")
    # for row in matrix:
    #     print(*row)

print(sum(sum(row) for row in matrix))
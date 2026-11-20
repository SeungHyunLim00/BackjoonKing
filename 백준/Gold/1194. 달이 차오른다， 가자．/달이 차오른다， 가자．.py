#달이 차오른다 가자
#1트 19:24 -> set에 dist를 포함해버려서 시간 터짐
#2트 : 19;40 -> key를 먹고 0처리 해버려서 두개 이상을 못먹는거 -> matrix 0 구문 없앰
# 어차피 key를 주운 '상태'로 관리하기 때문에 두번 이상 주울 걱정x

from  collections import deque

drdc = [(-1,0), (0,1), (1,0), (0,-1)]
inrange = lambda r, c : bool(0<=r<N and 0<=c<M)

N, M = map(int, input().split())
matrix = []
sr, sc = -1, -1

for r in range(N):
    matrix.append(list(input().strip()))
    for c, val in enumerate(matrix[-1]):
        if val == "0":
            sr, sc = r, c
            matrix[r][c] = '.'

# for row in matrix:
#     print(*row)

trans_door = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6}
trans_key = {key.lower() : val for key, val in trans_door.items()}

def bfs():
    q = deque()
    q.append((sr, sc, 0))

    vdict = dict()
    vdict[(sr, sc, 0)] = 0 # r, c,state  -> dist

    while q:
        cr, cc, state  = q.popleft()

        if matrix[cr][cc] == "1":
            return vdict[(cr,cc,state)]

        for dr, dc in drdc:
            nr, nc, nstate =  cr+dr, cc + dc, state


            if not inrange(nr,nc):
                continue

            val = matrix[nr][nc]
            if  val == "#" :
                continue

            if val in trans_door:
                if not (state & 1 << trans_door[val]):
                    continue # 해당하는 key가 없으면
            # key 있으면 진행 가능
            if val in trans_key:
                nstate |= 1 << trans_key[val]

            temp =  (nr, nc, nstate)
            if temp in vdict:
                continue

            q.append(temp)
            vdict[(nr,nc,nstate)] = vdict[(cr,cc,state)] + 1

    return -1

print(bfs())
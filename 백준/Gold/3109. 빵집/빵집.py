# 빵집
# 19:29 ~ 19:40 구상 11분
# 19:40 ~ 19:48 구현 8분
# 검증 제발 - 3분 -> 마지막에 찾았을 때 +1 해서 index error 발견
# 아 끝내면 안됨
# 총 디버깅 31분
	# 19:53 1차 제출 실패 -> 디버깅 15분
	# 20:09 2차 제출 실패 -> 시간초과 :
	# c-> r을 bit로 표현? 어쩌구 저쩌구 생각하다
	# appendleft 해서 우선순위로 따지면 되겠다 떠올림0-1 bfs? 어? FIFO?
	# 아 이거 dfs네
	# 20:09 ~ 20:24 bfs -> dfs 바꾸는데 15분
# 20:24 정답
# 구상을 대충한듯 ->
# 생각짧음 1. 처음에는 한 선이 막히면 그 아래는 볼 필요 없다 생각
# 생각짧음 2. 그다음에는 위부터 (-1,1), (0,1), (1,1) 중에 하나만 되면 된다고 생각-> 아님
# 생각짧음 3. 전부 다 보니까 visited에 즉시 반영 불가. vset으로 끌고다니기
# 생각짧음 4. vset때문에 시간 터져서 먼저 도착하면 다 끊어내야한다(가지치기) 이때 깨달음

# 리팩버전 - visited 즉시반영 -> R, C
R, C = map(int, input().split())
drdc = [(-1,1), (0,1), (1,1)]
inrange = lambda r, c : bool(0<=r<R and 0<=c<C)

matrix = []
for _ in range(R):
    matrix.append(input().strip())

ans = 0
visited = [[-1]*C for _ in range(R)]
start_r = 0

def solve(cr, cc, start_r):
    if cc == C-1:
        return 1

    for dr, dc in drdc:
        nr, nc = cr + dr, cc + dc
        if not inrange(nr,nc):
            continue
        if visited[nr][nc] != -1:
            continue
        if matrix[nr][nc] == "x":
            continue
        visited[nr][nc] = start_r
        if solve(nr,nc, start_r):
            return 1

    return 0

while True:
    if start_r >= R:
        break

    ans += solve(start_r, 0, start_r) # 아 set 안데리고 다녀도 되네

    start_r += 1

print(ans)
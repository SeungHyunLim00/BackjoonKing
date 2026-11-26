# 열쇠
#이미 풀엇던 문제라 구상 없이 들어감
# 열쇠를 먹고 지워야하는가? ㄴ
# 상태관리 -> 열쇠 먹은대로
#1초 -> bit로 하면 ㄱㅊ지 않을까?
# 상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나들 수 있다.
# 문서의 최대갯수 -> 아 귀찮은데 최대 10000인데 set이면 터지려나
# 아 3번째 예제 ) 문을 뚫고 들어가야 하는 경우도 있구나
# 두려울땐 시복 계산을 해보자
# 혹시 메모리 터지면 문서 좌표 -> 숫자 대응해서 저장하기 이것도 비트로
# 아니 문서 최대 갯수가 몇개인지는 알려줘야 할거 아냐
# 아 한 동선으로 먹을 수 있는게 아니고 전체 공유구나
# padding을 하면 범위를 좀 신경써
# 1트 - 메모리 초과
# 2트 - 동일, 메모리초과 ; q,vset, ans다 clear해도
# 1. 일단 로직에서 누수 없는지
# 2. 없으면 visited 배열 가능한지

# 다익처럼 한 좌표 -> 더 가진게 클 때만 아 그러면 bit가 아니라 set으로 갖고다녀야 하는디
# 비트가 아니고 열쇠가 커질때만?
# 최대 먹을 수 있는거니까 bit로 상태를 따질 필요가 없다


from  collections import deque


drdc = [(0,1), (1,0), (0,-1), (-1,0)]

TESTCASES = int(input())
vset = set()
key = set()
ans = set()
q = deque()

for testcase in range(1, TESTCASES + 1):
    vset.clear()
    ans.clear()
    key.clear()
    q.clear()

    N, M = map(int, input().split())
    inrange = lambda r, c : bool(0<=r<N+2 and 0<=c<M+2)

    def have_key(door, key):
        return door.lower() in key

    tot_get = 0
    matrix = ["."*(M+2)]
    for _ in range(N):
        matrix.append("."+input()+".") # split 안하고 함
        for val in matrix[-1]:
            if val == "$": tot_get += 1
    matrix.append("."*(M+2))
    al_bit = 0
    key.update(list(input().strip()))
    # 시작위치, state 잡기

    sr, sc= 0, 0

    q.append((0,0))
    vset.add((0,0))
    waiting = {chr(65 + i).lower() : [] for i in range(26)}
    while q:
        if len(ans) == tot_get: break
        cr, cc = q.popleft()

        for dr, dc in drdc:
            nr, nc = cr + dr, cc + dc

            if not inrange(nr,nc) : continue
            val = matrix[nr][nc]

            if (nr, nc) in vset: continue

            if val == "*":
                continue
            elif val == "$":
                ans.add((nr, nc))
            elif val.isalpha():
                if val.islower():
                    key.add(val)
                    if waiting[val]:
                        q.extend(waiting[val])
                else:
                    if not have_key(val, key):
                        waiting[val.lower()].append((nr, nc))
                        continue

            vset.add((nr,nc))
            q.append((nr,nc))

    print(len(ans))

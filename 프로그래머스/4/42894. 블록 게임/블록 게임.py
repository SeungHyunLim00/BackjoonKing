# 블록게임
# 구상 15분
# 마이너디버깅 : get poss에서 0을 찾으면 x 다른블록
# 1트 : 15:01 시간초과 -> sort해보기로 함. r을 위에서부터 하는게 최선일듯?
# 2 트 : 15:31 70점
# 15:49 backtrack이 아니라 위->아래 일수도
# 16:06 디버깅
# 블록이 5개인 경우 발견 -> 뭐지???? 아 break 걸어서 (ㄱㅊ음)
# 예제 참조를 못함
# assert로 결과만 참조하려고했는데 자기 자신 블록 오류는 아님

from collections import deque

drdc = [(1,0), (-1,0), (0,1), (0,-1)]
INF = int(1e9)

def solution(board):
    N = len(board)

    q = deque()
    visited = [[False] * N for _ in range(N)]
    blocks = 0
    empty = dict()
    cannot = set()

    for r in range(N):
        for c in range(N):
            if visited[r][c] or board[r][c] == 0:
                continue
            blocks += 1
            q.append((r, c))
            visited[r][c] = True
            num = board[r][c]

            minr, minc, maxr, maxc = INF, INF, -INF, -INF

            while q:
                cr, cc = q.popleft()
                minr, minc = min(minr, cr), min(minc, cc)
                maxr, maxc = max(maxr, cr), max(maxc, cc)

                for dr, dc in drdc:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < N and 0 <= nc < N):  continue
                    if visited[nr][nc]: continue
                    if board[nr][nc] == num:
                        q.append((nr, nc))
                        visited[nr][nc] = True

            # minmax 확정

            empty[num] = []
            # print(f"for {one} | r: {minr} - {maxr} | c: {minc} - {maxc}")

            for tr in range(minr, maxr + 1):
                for tc in range(minc, maxc + 1):
                    if board[tr][tc] != num:  # 빈칸
                        if 0 <= tr - 1 < N and board[tr-1][tc] == num: # 자기 위에 자신 -> 못함
                            cannot.add(num)
                            break
                        empty[num].append((tr, tc))  # 채워야할 곳(검은네모)

            if num in cannot:
                del empty[num]  # 선택 불가
    # print(cannot)
    newem = [(max(lst[0][0], lst[1][0]), num) for num, lst in empty.items()]
    newem.sort()  # minr 별로 sorting
    #print(newem)
    for _, num in newem:
        e1, e2 = empty[num]
        er1, ec1 = e1
        er2, ec2 = e2
        res1 = True
        for r in range(er1 + 1):  # er까지
            if board[r][ec1] > 0 and board[r][ec1] in cannot:
                cannot.add(num)
                res1 = False
                break
        if res1:
            for r in range(er2 + 1):
                if board[r][ec2] > 0 and board[r][ec2] in cannot:
                    cannot.add(num)
                    break

    return blocks - len(cannot)

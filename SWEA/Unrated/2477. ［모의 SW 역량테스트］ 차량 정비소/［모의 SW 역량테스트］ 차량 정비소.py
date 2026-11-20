
from collections import deque

TC = int(input())
for tc in range(1, TC+1):
    S, B, K, X, Y = map(int, input().strip().split())
    stime = list(map(int, input().strip().split()))# 접수
    btime = list(map(int, input().strip().split()))# 정비
    ktime = deque(enumerate(list(map(int, input().strip().split())), 1)) # cust_num, 도착 시간

    vst = [[0]*2 for _ in range(K+1)]# 정답 (접수창구 번호, 정비창구 번호)
    sst = [[0]*2 for _ in range(S+1)]# 접수 차있는지 (손님num, 끝나는시간)
    bst = [[0]*2 for _ in range(B+1)]# 정비 차있는지
    waiting = deque()
    cycle = ktime[0][1] # 젤 첫 도착부터 시작, 시간이다
    while True:
        for s in range(1, S+1): # 접수대 번호 작은 수부터
            if sst[s][1] <= cycle: # 접수 끝날 시간이면
                if sst[s][0]: # 이건 왜 보지?
                    waiting.append(sst[s][0]) # 접수대번호, 사람번호
                    sst[s][0] = 0
                    sst[s][1] = 0
                if ktime and ktime[0][1] <= cycle: # 도착한 이후면
                    num, _ = ktime.popleft()
                    vst[num][0] = s # 기입함
                    sst[s][0] = num # 손님번호
                    sst[s][1] = cycle + stime[s-1] # 끝나는시간

        for b in range(1, B+1):
            if bst[b][1] <= cycle:
                bst[b][0] = 0
                bst[b][1] = 0
                if waiting:
                    num = waiting.popleft()
                    vst[num][1] = b
                    bst[b][0] = num
                    bst[b][1] = cycle + btime[b-1]

        if not ktime and not sum(map(sum, sst)) and not waiting:
            break

        cycle += 1

    ans = 0
    for ki in range(1, K+1):
        if vst[ki] == [X, Y]:
            ans += ki

    print(f'#{tc} {ans if ans != 0 else -1}')
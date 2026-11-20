# 음악프로그램
# 만약 123 / 456 이렇게 되면 어쩌지? 아, 답이 여럿일 경우에는 아무거나 하나를 출력
# 순서 정하는게 불가능한 경우만 좀 생각해주면 됨
#10:09 ~ 11 읽기
# 바로 구현
# 10:22 정답
from  collections import deque
N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)] # 0번 x
input_cnt = [0]*(N+1) # 0번 x

for _ in range(M):
    lst = list(map(int, input().split()))
    num = 1
    for _ in range(lst[0]-1):
        from_ = lst[num]
        to_ = lst[num+1]
        adj_list[from_].append(to_)
        input_cnt[to_] += 1
        num += 1


q = deque()
for i in range(1, N+1):
    if input_cnt[i] == 0:
        q.append(i)

answer = []
while q:
    for _ in range(len(q)): # 이거 없으면 안되려나? 아닐듯
        cur = q.popleft()
        answer.append(cur)
        for nxt in adj_list[cur]:
            input_cnt[nxt] -= 1
            if input_cnt[nxt] == 0:
                q.append(nxt)

if len(answer) != N:
    print(0)
else:
    for ans in answer:
        print(ans)
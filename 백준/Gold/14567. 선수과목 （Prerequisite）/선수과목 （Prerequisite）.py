# Prerequisite
# Kahn alg
from collections import deque

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

chasu = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    chasu[B] += 1

q = deque()
for i in range(1, N + 1):
    if chasu[i] == 0:
        q.append(i)

ans = [0] * (N + 1)
dist = 0
while q:
    dist += 1
    for _ in range(len(q)):
        v = q.popleft()
        ans[v] = dist
        for nxt in adj_list[v]:
            chasu[nxt] -= 1
            if chasu[nxt] == 0:
                q.append(nxt)

print(*ans[1:])

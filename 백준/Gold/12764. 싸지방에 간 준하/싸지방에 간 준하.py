# 뭐야 이거 그거잖아
# 싸지방에 간 준하
# 16:50 독해 시작
# 1차제출 16:57
N = int(input())

humans = []
for _ in range(N):
    P, Q = map(int, input().split())
    humans.append((P, Q))

humans.sort() # 시작 순서대로 배열

def get_pc(start):
    if not pcs: return -1
    for i in range(len(pcs)):
        if pcs[i] <= start: return i
    return -1

pcs = []
usage = []
for start, end in humans:
    val = get_pc(start)
    if val == -1:
        pcs.append(end)
        usage.append(1)
    else:
        pcs[val] = end # 업데이트
        usage[val] += 1
print(len(pcs))
print(*usage)


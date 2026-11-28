# 2x2x2 큐브
# 아 두개씩 밀어야하는데 까먹음
# 그 접히는 부분 빼먹음
# 1차 제출 실패
# 아 아 회전 두개 빼먹었다 :
lst = [None] + list(map(int, input().split()))

idxs_lists = [
        [13,14,5,6,17,18,21,22],
        [15,16,7,8,19,20,23,24],
        [1,3,5,7,9,11,24, 22 ],
        [2,4,6,8,10,12, 23, 21 ],
        [3, 4,17, 19, 10, 9, 16, 14],
        [1, 2, 18, 20, 12, 11, 15, 13]
        ]

def check(aft):
    for i in range(1, 25, 4):
        if aft[i] == aft[i+1] == aft[i+2] == aft[i+3]: continue
        else: return False
    return True

def solve():
    for idxs in idxs_lists:
        # 좌?
        aft = lst[:]
        for i, idx in enumerate(idxs):
            aft[idx] = lst[idxs[(i+2)%len(idxs)]]
        if check(aft): return True

        aft = lst[:]
        for i, idx in enumerate(idxs):
            aft[idx] = lst[idxs[(i-2)%len(idxs)]]
        if check(aft): return True
    return False

print(1) if solve() else print(0)
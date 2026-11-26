# RBY 팡!
# 투포인터 식으로 하면 되려나?
# 19:15 ~ 19:25 구상
# "소멸하지 않고 남아있는 공의 수 최소화" -> 이게 뭔말이지?
# 아예 다 소멸하면 안친다 로 이해함
# 19:53 다맞긴 했는데 좀 쎄함
# 검증 ㄱㄱ
# 10000 케이스에서 시간은 문제없어보임
# 1 케이스 -> continue indentation 잘못한거 잡음

# DEBUG = True
#
# def myprint(string):
#     if not DEBUG: return
#     print(f"======={string}==========")
#     for b in BALLS:
#         print(trans[b])
# trans = {1:'R', 2:'B', 3:'Y'}

N = int(input())

BALLS = []
for _ in range(N):
    BALLS.append(int(input()))
#myprint("initial")

def pang(start_, color):
    up = start_ - 1
    down = start_ + 1
    c = color
    trial = 0
    length = 0
    while True:
        trial += 1
        temp_len = 1 if trial == 1 else 0
        while up >= 0 and BALLS[up] == c:
            up -= 1
            temp_len += 1
        while down < N and BALLS[down] == c:
            down += 1
            temp_len += 1

        if temp_len < 4 : break

        length += temp_len
        if up < 0 or down >= N : break
        if BALLS[up] == BALLS[down]:
            c = BALLS[up]
        else:
            break

    #print(f"for change {start}th : {trans[BALLS[start_]]} -> {trans[color]} : return {N - length}")
    #if length == N: return N -> 이거>????
    return N - length


min_ans = N
for start in range(N):
    if start == 0:
        if N > 1 and BALLS[1] != BALLS[0]:
            min_ans = min(min_ans, pang(start, BALLS[1]))
        continue
    if start == N-1:
        if N > 1 and BALLS[start-1] != BALLS[start]:
            min_ans = min(min_ans, pang(start, BALLS[start-1]))
        continue
    # 중간거면
    if BALLS[start - 1] != BALLS[start]:
        min_ans = min(min_ans, pang(start, BALLS[start - 1]))
    if BALLS[start + 1] != BALLS[start]:
        min_ans = min(min_ans, pang(start, BALLS[start + 1]))
print(min_ans)
# 19:05 구상 시작
# 19:16 구현 시작
# 유사 스도쿠
# 19:42 테케 10개 검증


coord_to_line = {      (0,4): [4,6],
    (1,1):[1,2], (1,3):[1,4], (1,5):[1,6], (1,7):[1,3],
            (2,2):[2,4],               (2,6):[3,6],
    (3,1):[4,5], (3,3) : [2,5], (3,5):[3,5], (3,7):[5,6],
                       (4,4): [2,3]
                 }
line_sum = [0] * 7  # 0번 비워둠
line_count = [0] * 7 # 0 번 비워둠

# 아 A =>  1 바꾸는거 생각 안남
trans = {chr(64 + i) : i for i in range(1, 13) }
rev_trans = {val:key for key, val in trans.items()}
used = [0]*13 # 0번 안씀

empty = []
matrix = []
for x in range(5):
    matrix.append(list(input().strip()))

    for y, val in enumerate(matrix[-1]):
        if val == "x":
            empty.append((x, y))
        elif val != ".":
            for line in coord_to_line[(x, y)]:
                line_sum[line] += trans[val]
                used[trans[val]] = 1
                line_count[line] += 1

found = None
answer = []
def back(idx):
    global found
    if found is not None:
        return

    if idx == len(empty):
        found = answer[:]
        return

    x, y = empty[idx]
    for i in range(1, 13):
        if used[i]:
            continue
        for line in coord_to_line[(x,y)]:
            if line_count[line] + 1 > 4:
                break
            if line_sum[line] + i > 26:
                break
        else:
            for line in coord_to_line[(x, y)]:
                line_count[line] += 1
                line_sum[line] += i
            used[i] = 1
            answer.append(i)
            back(idx + 1)

            # 원복
            for line in coord_to_line[(x, y)]:
                line_count[line] -= 1
                line_sum[line] -= i
            used[i] = 0
            answer.pop()


back(0)

for ith, (x,y) in enumerate(empty):
    matrix[x][y] = rev_trans[found[ith]]

for row in matrix:
    print(''.join(row))
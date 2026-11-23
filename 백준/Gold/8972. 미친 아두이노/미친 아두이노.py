# 미친 아두이노
# 14:42 독해, 14:44 구현

drs = [ 1, 1, 1, 0, 0, 0, -1, -1, -1]
dcs = [-1, 0, 1, -1,0, 1, -1, 0,   1]
getdist = lambda r1, c1, r2, c2 : abs(r1-r2) + abs(c1 - c2)
INF = int(1e9)
R, C = map(int, input().split())
inrange = lambda r, c : bool(0<=r<R and 0<=c<C)

def myprint():
    #print(f"========={string}=========")
    for r in range(R):
        for c in range(C):
            if (r,c) in mads:
                print(f"R", end = "")
            elif r == cr and c == cc:
                print("I", end = "")
            else:
                print(f".", end = "")
        print()

jr, jc = -1, -1
mads = set()
for r in range(R):
    for c, val in enumerate(list(input().strip())):
        if val == "I":
            jr, jc = r, c
        elif val == "R":
            mads.add((r,c))

cr, cc = jr, jc
stop_flag = False

for turn, order in enumerate(list(map(int, input().strip())), 1):
    dr, dc = drs[order-1], dcs[order-1]
    cr, cc = cr + dr, cc + dc # 보드를 벗어나는 입력은 x

    if (cr,cc) in mads: stop_flag = True; print(f"kraj {turn}"); break

    new_mads = set()
    rm_set = set()
    for r, c in mads:
        orig = getdist(r, c, cr, cc)
        comp = (INF, INF, INF)
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not inrange(nr,nc): continue
            new = getdist(cr, cc, nr, nc)
            if new >= orig: continue
            temp = (new, nr, nc)
            if temp < comp: comp = temp
        dist, nr, nc = comp
        if dist == 0: stop_flag = True ; print(f"kraj {turn}") ;  break
        if (nr, nc) in new_mads: rm_set.add((nr, nc))
        new_mads.add((nr,nc))

    if stop_flag: break

    for r, c in rm_set:
        new_mads.remove((r,c))

    mads = new_mads

if not stop_flag:
    myprint()

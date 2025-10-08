from collections import deque

def valid(m,c): 
    return m==0 or m>=c   # Safe if missionaries >= cannibals

def bfs():
    start=(3,3,1)   # (M_left, C_left, boat)
    goal =(0,0,0)
    q=deque([(start,[])])
    seen=set()
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]

    while q:
        (m,c,b), path=q.popleft()
        if (m,c,b)==goal: return path+[(m,c,b)]
        if (m,c,b) in seen: continue
        seen.add((m,c,b))

        for mm,cc in moves:
            if b: new=(m-mm,c-cc,0)   # Boat to right
            else: new=(m+mm,c+cc,1)   # Boat to left
            m2,c2,_=new
            if 0<=m2<=3 and 0<=c2<=3 and valid(m2,c2) and valid(3-m2,3-c2):
                q.append((new,path+[(m,c,b)]))

for step in bfs():
    print(step)

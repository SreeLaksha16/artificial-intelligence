from collections import deque
def water_jug(x,y,t):
    q=deque([(0,0)]); seen=set()
    while q:
        a,b=q.popleft()
        if (a,b) in seen: continue
        print(a,b)
        if a==t or b==t: return
        seen.add((a,b))
        q.extend([(x,b),(a,y),(0,b),(a,0),
                  (a-min(a,y-b), b+min(a,y-b)),
                  (a+min(b,x-a), b-min(b,x-a))])

water_jug(4,3,2)
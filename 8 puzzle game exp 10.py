from collections import deque
def bfs(start, goal):
    q, seen = deque([(start, [])]), set()
    while q:
        state, path = q.popleft()
        if state == goal: return path+[state]
        seen.add(state)
        i = state.index(0)
        for m in (-3,3,-1,1):
            j = i+m
            if 0<=j<9 and not(i%3==2 and m==1 or i%3==0 and m==-1):
                new = list(state); new[i],new[j]=new[j],new[i]
                t = tuple(new)
                if t not in seen: q.append((t,path+[state]))
start = (1,2,3,4,0,5,6,7,8)
goal  = (1,2,3,4,5,6,7,8,0)
for s in bfs(start, goal): print(s[0:3],"\n",s[3:6],"\n",s[6:9],"\n")
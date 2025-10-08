import itertools
g=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
p=range(4);m=1e9;r=[]
for perm in itertools.permutations(p[1:]):
    c=0;k=0
    for j in perm:c+=g[k][j];k=j
    c+=g[k][0]
    if c<m:m=c;r=perm
print("Route:",(0,)+r+(0,),"Cost:",m)

cols=['R','G','B']
adj={'A':['B','C'],'B':['A','C'],'C':['A','B']}
def safe(n,c,a):return all(a.get(x)!=c for x in adj[n])
def solve(a={}):
    if len(a)==len(adj):return a
    n=[x for x in adj if x not in a][0]
    for c in cols:
        if safe(n,c,a):a[n]=c;r=solve(a)
        if r:return r;a.pop(n)
print("Solution:",solve())

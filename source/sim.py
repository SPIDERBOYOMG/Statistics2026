import numpy as np, json
N,K,n=6,3,60
rng=np.random.default_rng(2026)
urn=np.array([1]*K+[0]*(N-K))
rows=[]
for t in range(1,n+1):
    d=rng.choice(N,size=2,replace=False)
    rows.append((t,int(d[0])+1,int(d[1])+1,int(urn[d[0]]),int(urn[d[1]])))
x=np.array([r[3] for r in rows]);y=np.array([r[4] for r in rows])
print(x.mean(),y.mean(),x.var(ddof=1),y.var(ddof=1),np.cov(x,y,ddof=1)[0,1],np.corrcoef(x,y)[0,1])
for a in (0,1):
  for b in (0,1): print(a,b,((x==a)&(y==b)).sum())
json.dump(rows,open('rows.json','w'))
big=np.random.default_rng(1)
M=200000
a=np.array([big.permutation(6)[:2] for _ in range(M)])
u=(a<3).astype(int)  # first 3 labels red
print(np.corrcoef(u[:,0],u[:,1])[0,1],u.mean(0))

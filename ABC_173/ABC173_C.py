import numpy as np
from itertools import combinations
h,w,k = map(int,input().split())
c = np.empty((h,w))
for i in range(h):
    c[i,:] = np.array(list(map(int,input().replace(".",'0 ').replace("#",'1 ').split())))

cnt = 0
row,col = range(h),range(w)

for i in range(1,h+1):
    for j in range(1,w+1):
        if i==h and j==w:
            break
        for x in combinations(row, i):
            for y in combinations(col,j): 
                s = c[np.array(x),:]
                s = s[:,np.array(y)].sum()
                if s==k:
                    cnt+=1
if c.sum()==k:cnt+=1
print(cnt)
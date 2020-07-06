import numpy as np
n,k = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True,key=lambda x: abs(x))

def main(n,k,a):
    a = np.array(a)
    if (a<0).all() and k%2==1 : return np.prod(a[-1*k:])
    prod_idx = list(range(k))
    if np.prod(2*(a[prod_idx]>0)-1)>0:
        prod = 1
        for i in prod_idx:
            prod = (prod*a[i])%1000000007
        return prod
    else:
        p_1 = prod_idx
        p_1_new = []
        for i in range(k-1,-1,-1):
            if a[i]<0:
                p_1.remove(i)
                p_1_new.append(i)
                break
        for i in range(k,len(a)):
            if a[i]>0:
                p_1.append(i)
                p_1_new.append(i)
                break
        p_2 = prod_idx
        p_2_new = []
        for i in range(k-1,-1,-1):
            if a[i]>0:
                p_2.remove(i)
                p_2_new.append(i)
                break
        for i in range(k,len(a)):
            if a[i]<=0:
                p_2.append(i)
                p_2_new.append(i)
                break
        if len(p_1_new)==2 and len(p_2_new)==2:
            if abs(p_1_new[0]*p_2_new[1]) <= abs(p_2_new[0]*p_1_new[1]):
                prod = 1
                for i in p_2:
                    prod = (prod*a[i])%1000000007
                return prod
            else:
                prod = 1
                for i in p_1:
                    prod = (prod*a[i])%1000000007
                return prod
        if len(p_1_new)==2:
            prod = 1
            for i in p_1:
                prod = (prod*a[i])%1000000007
            return prod
        else:
            prod = 1
            for i in p_2:
                prod = (prod*a[i])%1000000007
            return prod


        


print(main(n,k,a)%1000000007)
from collections import deque
import numpy as np
n,m,k = map(int,input().split())
A = deque(map(int,input().split()))
B = deque(map(int,input().split()))

a=[0]
b = [0]
for i in range(n):
    a.append(a[i]+A[i])
for i in range(m):
    b.append(b[i]+B[i])

x,j = 0,m
for i in range(n+1):
    if a[i]>k:
        break
    while b[j] > k-a[i]:
        j -=1
    x = max(x,i+j)
print(x)


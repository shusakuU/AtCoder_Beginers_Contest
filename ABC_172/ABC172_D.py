n = int(input())
c = 0
for i in range(1,n+1):
    t = n//i
    c += i*t*(t+1)//2
print(c)
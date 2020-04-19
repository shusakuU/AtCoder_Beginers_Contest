def A():
    k = int(input())
    print(((k+1)//2)*(k//2))

def B():
    x1,y1,x2,y2 = map(int,input().split())
    diffx,diffy = x2-x1,y2-y1
    x3,y3 = x2-diffy, y2+diffx
    x4,y4 = x3-diffx, y3-diffy
    print(x3,y3,x4,y4)

def C():
    n,k = map(int,input().split())
    k_divisor = n//k
    ans = k_divisor**3
    if k%2==0:
        half_k_divisor = (n//k)+int(n%k>=k/2)
        ans += half_k_divisor**3
    print(ans)

def D():
    pass



if __name__ == '__main__':
    problem_kind = input('What problem? Choose A,B,C or D\n')
    if   problem_kind == 'A': A()
    elif problem_kind == 'B': B()
    elif problem_kind == 'C': C()
    else : D()

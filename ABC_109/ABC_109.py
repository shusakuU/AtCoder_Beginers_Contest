def A():
    A,B = map(int,input().split())
    print('Yes' if (A*B)%2==1 else 'No')

def B():
    n = int(input())
    words = []
    flag = True
    for i in range(n):
        words.append(input())
    for i in range(1,n):
        if words[i][0] != words[i-1][-1]:
            flag = False
            break
    if len(set(words)) != n:
        flag = False
    print('Yes' if flag else 'No')

def GCD(x,y):
    if y>x :
        x,y = y,x
    mod = x%y
    return GCD(y,mod) if mod!=0 else y

def C():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    for i in range(N-1,0,-1):
        x[i] = abs(x[i]-x[i-1])
    x[0] = abs(x[0]-X)
    gcd = x[0]
    for i in range(1,N):
        gcd = GCD(gcd,x[i])
    print(gcd)


def D():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        if i %2==0:
            a += list(map(int,input().split()))
        else:
            a += list(reversed(list(map(int,input().split()))))
    operations = []
    ope_flag = False
    idx = 0
    ope_temp = ''
    cnt = 0
    for row in range(h):
        columns = range(w) if row%2==0 else reversed(range(w))
        for col in columns:
            if ope_flag:
                ope_temp += ' {0} {1}'.format(row+1,col+1)
                operations.append(ope_temp)
                ope_temp=''
                ope_flag=False
                a[idx]+= 1
            mod = a[idx]%2
            if mod==1:
                ope_temp = '{0} {1}'.format(row+1,col+1)
                ope_flag= True
            idx += 1
            cnt += mod
    print(len(operations))
    for i in range(len(operations)):
        print(operations[i])





if __name__ == '__main__':
    problem_kind = input('What problem? Choose A,B,C or D\n')
    if   problem_kind == 'A': A()
    elif problem_kind == 'B': B()
    elif problem_kind == 'C': C()
    else : D()

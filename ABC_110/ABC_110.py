def A():
    a = list(map(int,input('').split()))
    print(max(a)*9+sum(a))

def B():
    n,m,x,y = map(int,input('').split())
    max_x = max(list(map(int,input('').split()))+[x])
    min_y = min(list(map(int,input('').split()))+[y])
    if max_x < min_y :
        print('No War')
    else:
        print('War')

def C():


def D():
    pass








if __name__ == '__main__':
    #= map(int,input().split())
    problem_kind = input('What problem? Choose A,B,C or D\n').upper()
    if   problem_kind == 'A': A()
    elif problem_kind == 'B': B()
    elif problem_kind == 'C': C()
    else : D()

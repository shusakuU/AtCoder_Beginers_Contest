def A():
    pass

def B():
    pass

def C():
    pass

def D():
    pass








if __name__ == '__main__':
    #= map(int,input().split())
    problem_kind = input('What problem? Choose A,B,C or D\n').upper()
    if   problem_kind == 'A': A()
    elif problem_kind == 'B': B()
    elif problem_kind == 'C': C()
    else : D()

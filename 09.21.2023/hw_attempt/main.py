# fmt:off
t=int(input())
if t==2:
    a=int(input())
    b=int(input())
    h=input()
    if h=='+':
        print(a+b)
    elif h=='-':
        print(a-b)
    else:
        print(a/b)
elif t==3:
    a=int(input())
    b=int(input())
    c=int(input())
    h=input()
    if h=='+':
        print(a+b+c)
    elif h=='-':
        print(a-b-c)
    else:
        print(a/b/c)
elif t==4:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    h=input()
    if h=='+':
        print(a+b+c+d)
    elif h=='-':
        print(a-b-c-d)
    else:
        print(a/b/c/d)
# fmt:on

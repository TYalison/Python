for i in range(100,10000000):
    num=str(i)
    num=list(num)
    n=len(num)
    result=0
    for j in range(n):
        result+=int(num[j])**n
    if result==i:
        print(i)

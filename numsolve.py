def cal(a,b,c,d,x):
    res=a*(x**3)+b*(x**2)+c*x+d
    return res
def NumSolve():
    num=0
    print("给出方程中各项的系数:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    d=int(input("d="))
    print("方程的三个不同实根为:")
    for i in range(-100,100):
        resl=cal(a,b,c,d,i)
        resr=cal(a,b,c,d,i+1)
        if resl==0:
            print("%.2f"%i)
            num+=1
            if num==3:
                return
            continue
        elif resl*resr<0:
            low=i
            high=(i+1)
            while low<high:
                mid=(low+high)/2
                resl=cal(a,b,c,d,low)
                resr=cal(a,b,c,d,high)
                res=cal(a,b,c,d,mid)
                if abs(res)<1e-4:
                    print("%.2f"%mid)
                    num+=1
                    if num==3:
                        return
                    break
                if resl*res<0:
                    high=mid
                    if res*resr<0:
                        low=mid
                    if abs(high-low)<1e-4:
                        print("%.2f"%mid)
                        num+=1
                        if num==3:
                            return
    return
NumSolve()

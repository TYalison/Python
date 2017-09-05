def getInput():
    l=[]
    print("从键盘连续输入一组数据")
    print("请用空格键结束输入")
    while(True):
        b=input()
        if b==" ":
            break
        else:
            l.append(int(b))
    return l
def binarySearch(l,key):
    if len(l)==0:
        return -1
    elif len(l)==1:
        if key==l[0]:
            return 0
        else:
            return -1
    else:
        n=int(len(l)/2)
        while (n>0)and(n<len(l)):
            if key==l[n]:
                return n
            elif key<l[n]:
                if int(n/2)<n:
                    n=int(n/2)
                else:
                    n-=1
                continue
            else:
                if int((len(l)+n)/2)>n:
                    n=int((len(l)+n)/2)
                else:
                    n+=1
                continue
        if (n<0)or(n>(len(l)-1)):
            return -1
        elif key==l[n]:
            return n
        else:
            return-1
if __name__=="__main__":
    l=getInput()
    key=int(input("输入要查找的数据:"))
    result=binarySearch(l,key)
    if result==-1:
        print("未找到!")
    else:
        print("要查找的数据在输入序列中的编号为:%d"%result)

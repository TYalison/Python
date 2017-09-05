List=[]
def ShellSort(List):
    print("输入对应12个月的需要排序的数据:")
    for i in range(12):
        List.append(int(input()))
    mid=6
    while mid>=1:
        for m in range(mid,12):
            tmp=List[m]
            pos=m
            for n in range(m-mid,-1,-mid):
                if List[n]>tmp:
                    List[n+mid]=List[n]
                    pos=n
            List[pos]=tmp
        mid=int(mid/2)
    print("输入的数据按从小到大排序为:")
    for j in range(12):
        print("%d"%List[j])
    return
ShellSort(List)

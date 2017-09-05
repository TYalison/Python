List=[]
def InsertSort(List):
    print("输入对应12个月的需要排序的数据:")
    for i in range(12):
        List.append(int(input()))
    for p in range(12):
        tmp=List[p]
        pos=p
        for q in range(p-1,-1,-1):
            if List[q]>tmp:
                List[q+1]=List[q]
                pos=q
        List[pos]=tmp
    print("输入的数据按从小到大排序为:")
    for j in range(12):
        print("%d"%List[j])
    return
InsertSort(List)

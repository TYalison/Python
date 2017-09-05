List=[]
def SelectSort(List):
    print("输入对应12个月的需要排序的数据:")
    for i in range(12):
        List.append(int(input()))
    for m in range(12):
        minL=m
        for n in range(i,12):
            if List[n]<List[minL]:
                minL=n
        List[m],List[minL]=List[minL],List[m]
    print("输入的数据按从小到大排序为:")
    for j in range(12):
        print("%d"%List[j])
    return
SelectSort(List)

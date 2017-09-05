List=[]
def BubbleSort(List):
    print("输入对应12个月的需要排序的数据:")
    for i in range(12):
        List.append(int(input()))
    for m in range(12):
        for n in range(1,12):
            if List[n-1]>List[n]:
                List[n-1],List[n]=List[n],List[n-1]
    print("输入的数据按从小到大排序为:")
    for j in range(12):
        print("%d"%List[j])
    return
BubbleSort(List)

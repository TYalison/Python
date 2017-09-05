def locate(L):
    maxwor=L[0][-1]
    for i in range(1,len(L)):
        if L[i][-1]>maxwor:
            maxwor=L[i][-1]
            k=i
    return k
n=5
weight=[2,2,6,5,4]
worth=[6,3,5,4,6]
limit=10
temp=[]
deal=[]
for i in range(n):
    for j in range(1,n):
        swei=weight[i]+weight[j]
        if swei>limit:
            continue
        else:
            swor=worth[i]+worth[j]
            temp.append([i,j,swor])
if len(temp)==0:
    for i in range(n):
        if weight[i]<=10:
            swor=worth[i]
            break
    q=i
    for j in range(i+1,n):
        if (swor<worth[j])and(weight[j]<=limit):
            swor=worth[j]
            q=j
    if (i==(n-1))and(weight[i]>10):
        print("背包为空!")
    else:
        print("将编号为%d的物品放入背包，其价值为%d!"%(q,swor))
else:
    num=2
    Th=[]
    deal=temp[locate(temp)]
    for i in range(len(temp)):
        for j in range(temp[i][-2]+1,n):
            swei=weight[temp[i][0]]+weight[temp[i][1]]+weight[j]
            if swei>limit:
                continue
            else:
                swor=temp[i][-1]+worth[j]
                m=[temp[i][0],temp[i][1],j,swor]
                Th.append(m)
    while (len(Th)>0)and(num<n):
        num+=1
        temp=Th
        deal=temp[locate(temp)]
        m=[]
        Th=[]
        swei=0
        for i in range(len(temp)):
            for j in range(temp[i][-2]+1,n):
                for k in range(len(temp[i])-1):
                    swei+=weight[temp[i][k]]
                swei+=weight[j]
                if swei>limit:
                    continue
                else:
                    swor=temp[i][-1]+worth[j]
                    for k in range(len(temp[i])-1):
                        m.append(temp[i][k])
                    m.append(j)
                    m.append(swor)
                    Th.append(m)
        if (num==n)and(len(Th)>0):
            deal=Th[locate(Th)]
    print("装入背包的物品对应编号为:")
    print(deal[0:-1])
    print("其总价值为%d"%deal[-1])

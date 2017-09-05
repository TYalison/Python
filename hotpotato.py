peonum=input("输入玩家人数：")
peonum=int(peonum)
queue=[]
for i in range(peonum):
    name=input("输入玩家名称：")
    queue.append(name)
num=input("输入计数常量：")
num=int(num)
def hotpotato(queue,num):
    i=0
    while len(queue)>1:
        if i==num:
            queue.pop(0)
            i=0
        else:
            queue.append(queue[0])
            queue.pop(0)
            i+=1
    print("最终剩余玩家：%s"%queue[0])
hotpotato(queue,num)

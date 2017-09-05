def paint(mat,num,result):
    for i in range(num):
        result.append(1)
    for i in range(num):
        for j in range(num):
            while (mat[i][j]==1)and(result[i]==result[j]):
                if j>i:
                    result[j]+=1
                    if result[j]==5:
                        result[j]=1
                else:
                    result[i]+=1
                    if result[i]==5:
                        result[i]=1
    return result
if __name__=="__main__":
    mat=[[0,1,0,0,0,0,1],
         [1,0,1,1,1,1,1],
         [0,1,0,1,0,0,0],
         [0,1,1,0,1,0,0],
         [0,1,0,1,0,1,0],
         [0,1,0,0,1,0,1],
         [1,1,0,0,0,1,0]]
    num=len(mat)
    result=[]
    print("对应编号0~%d的省份的填色方案为:"%num)
    print(paint(mat,num,result))

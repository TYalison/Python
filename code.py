List=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=3
def code(string,shift):
    l=list(string)
    for i in range(len(string)):
        for j in range(26):
            if l[i]==List[j]:
                if j+shift<26:
                    l[i]=List[j+shift]
                    j=0
                    break
                else:
                    l[i]=List[j+shift-26]
                    j=0
                    break
    print("暗文：%s"%(''.join(l)))
string=input("明文：")
string=string.lower();
code(string,k);

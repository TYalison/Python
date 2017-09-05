String=input("输入一行字符串：")
String=list(String)
List=[]
Dict={')':'(',']':'[','>':'<','}':'{'}
def match(String,List):
    for i in range(len(String)):
        if (String[i]=='(')or(String[i]=='[')or(String[i]=='<')or(String[i]=='{'):
            List.append(String[i])
        elif (String[i]==')')or(String[i]==']')or(String[i]=='>')or(String[i]=='}'):
            if (len(List)>0)and(List[len(List)-1]==Dict[String[i]]):
                List.pop()
            else:
                print("no")
                return
    if len(List)==0:
        print("yes")
        return
match(String,List);

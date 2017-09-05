dict={}
def add_dict(dictionary,en,ch):
    dictionary[en]=ch
    dictionary[ch]=en
    print("添加成功")

for i in range(10):
    en=input("增添的英文单词:")
    ch=input("对应的中文单词:")
    add_dict(dict,en,ch);
    
def find(dictionary,string):
    if string in dictionary:
        print("该单词的意思是:%s"%dictionary[string])
    else:
        print("该单词不在dict内")

    

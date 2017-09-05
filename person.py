# 要求：
# 构建一个类，用来标记一个基本的“人”的概念；
# 需要拥有2个属性，姓名和年龄；
# 需要具备两个行为，一个行为是过生日（年龄加1）、一个行为是点名（返回姓名）
# 年龄、姓名都是私有属性，类外部不可直接访问；
# 类具备初始化功能（__init__）,使用者可以对姓名、年龄都进行赋初值操作，也可以仅仅对于姓名赋值，此时默认年龄是 20 岁

class Person:
    name=''
    age=20
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def LeadBirthday(self):
        self.age+=1
    def RollCall(self):
        print('%s'%(self.name))
Name=input("姓名：")
Age=input("年龄：")
Age=int(Age)
info=Person(Name,Age)
info.LeadBirthday()
print(info.age)
info.RollCall();

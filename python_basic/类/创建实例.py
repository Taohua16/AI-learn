class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("张三",18,"男")
p2 = Person("王五",19,"女")


# 通过 实例._dict_ 可以查看实例身上所有属性
print(p1.__dict__)

print(p2.name)

print(type(p1))
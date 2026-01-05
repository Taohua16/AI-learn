# 多态概念：父类定义一个方法，而子类去实现这个方法，这样，我们就通过父类创建的对象，调用这个方法，就会执行子类的方法。
# 标准多态： 1、继承关系 2、重写方法 3、类型限制要写父类
from symtable import Class


class Animal:
    def speak(self):
        print("发声")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")

def make_sound(amimal:Animal):#类型注解
        amimal.speak()

# 鸭子多态：1、继承关系 2、方法名相同 3、参数个数相同 4、参数顺序相同 5、返回值相同
# 不检查对象类型，只关注是否能做某件事

class Fish:
    def speak(self):
        print("发出水泡")

class Pig:
    def speak(self):
        print("哼哼哼")

def make_sound2(amimal):
    amimal.speak()

# c1 = Fish ()
# c2 = Pig()
#
# make_sound2(c1)
# make_sound2(c2)

# 抽象类：不能直接实例化，通常作为规范，让子类继承，必须定义其中的抽象方法
from abc import ABC,abstractmethod

class MustRun(ABC):
    @abstractmethod
    def run(self):
        print("跑")


from datetime import datetime
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    count = 0
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        Student.count += 1
        self.stu_id = f'{datetime.now().year}{Student.count:04d}'
        self.scores = {}

    def add_score(self,subject,socre):
        self.scores[subject] = socre

    def calcu_avg(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores.values())/len(self.scores)

    def __str__(self):
        return f'{self.name} {self.age} {self.gender} {self.stu_id} {self.scores} {self.calcu_avg()}'

class Manager:
    def __init__(self):
        self.stu_list = []

    def add_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        gender = input("请输入性别：")
        stu = Student(name,age,gender)
        self.stu_list.append(stu)
        print(f'添加成功！学号为：{stu.stu_id}')

    def del_student(self):
        sid = input("请输入学号：")
        for stu in self.stu_list:
            if stu.stu_id == sid:
                self.stu_list.remove(stu)
                print("删除成功！")
                return
        print("没有此学号！")
        return

    def show_all(self):
        for stu in self.stu_list:
            print(stu)

    def set_score(self):

        sid = input("请输入学号：")
        for stu in self.stu_list:
            if stu.stu_id == sid:
                score_str = input("请输入成绩：(学科-成绩，学科-成绩)")
                score_list = score_str.replace('，',',').split(',')
                for score in score_list:
                    subject,score = score.split('-')
                    stu.add_score(subject,int(score))
                print("添加成功！")
                return
        print("没有此学号！")
        return
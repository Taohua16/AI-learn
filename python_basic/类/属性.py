from datetime import datetime

class Person:
    def __init__(self,name,age,gender):
        # 实例属性
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("张三",18,"男")
p2 = Person("王五",19,"女")



# 类属性
class Person:
    # 类属性 1. 保持在类身上 2. 可以通过类和实例访问 3. 保存公共数据
    country = "中国"
    planet = "地球"
    max_age = 120
    def __init__(self,name,age,gender):
        # 实例属性
        self.name = name
        self.age = age
        self.gender = gender

    # 类方法
    # 操作类级别信息，工厂方法
    @classmethod
    def change_country(cls,value):
        cls.country = value

    # 工厂方法 通过类身上的方法创建实例
    @classmethod
    def create(cls,info_str):
        name,year,gender = info_str.split("-")
        current_year = datetime.now().year
        age = current_year - int(year)
        return cls(name,age,gender)

    # 静态方法
    # 1. 类身上 2.不收到self和cls参数，只有自定义参数 3.不会访问类和实例相关内容 4.一般为类相关的工具方法
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - int(year)
        return age >= 18

class Student(Person):
    def __init__(self,name,age,gender,grade):
        super().__init__(name,age,gender)
        self.grade = grade
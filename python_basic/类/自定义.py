class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 自定义方法
    # 调用实例对象（self），打印属性
    def speak(self,msg):
        print("我叫··%s,今年%d岁,性别%s"%(self.name,self.age,self.gender))
        print(msg)
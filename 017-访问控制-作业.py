# 访问控制-作业

# 构造一个“学生”类，包含：姓名、性别、年龄等属性和“学习”方法
# 将年龄设置为私有变量，用set和get方法赋值和取值
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.__age = age
        self.sex = sex

    def get_age(self):
        print(f"{self.name} 的年龄是：{self.__age}")

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("年龄有误，请重新设置")


wutinghan = Student("吴听寒", 23, "女")
wutinghan.get_age()
wutinghan.set_age(-1)
wutinghan.get_age()
wutinghan.set_age(24)
wutinghan.get_age()


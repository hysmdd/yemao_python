# 类的定义和使用

# 构造一个学生类，包括身高、体重属性，“学习”方法
class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def study(self):
        print(f"{self.name}正在学习...")


# 实例化一个对象“吴听寒”
wutinghan = Student("吴听寒", 165, 100)

# 访问该实例的属性和方法
print(f"姓名：{wutinghan.name}")
print(f"身高：{wutinghan.height}")
print(f"体重：{wutinghan.weight}")
wutinghan.study()


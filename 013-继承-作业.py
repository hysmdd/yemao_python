# 继承-作业

# 构造一个父类学生，包含“学习”方法
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def study(self):
        print(f"{self.name}正在学习")


# 构造继承类“人工智能专业学生”，包含方法“编程“
class AiStudent(Student):
    def programming(self):
        print(f"机器人专业学生{self.name}正在编程")


# 构造继承类“机器人专业学生”，包含方法“设计”
class RobotStudent(Student):
    def design(self):
        print(f"机器人专业学生{self.name}正在设计")

# 构造不同类的对象，对各自方法进行调用
luoxiaoyang = AiStudent('洛小阳', 18, '男')
luoxiaoyang.study()
luoxiaoyang.programming()

zhangpolu = RobotStudent("张破虏", 24, "男")
zhangpolu.study()
zhangpolu.design()



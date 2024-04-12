# 派生-作业

# 构造一个父类“学生”，包含：姓名、性别、年龄等属性和”学习“方法
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def learn(self):
        print(f"{self.name}正在学习...")


# 构造继承类“人工智能专业学生“，派生出新的属性”分数“
class AiStudent(Student):
    def __init__(self, name, age, sex, score):
        super().__init__(name, age, sex)
        self.score = score


# 在实例中使用这些属性
wutinghan = AiStudent('吴听寒', 23, '女', 100)
print(f"姓名：{wutinghan.name}")
print(f"年龄：{wutinghan.age}")
print(f"性别：{wutinghan.sex}")
print(f"分数：{wutinghan.score}")
wutinghan.learn()

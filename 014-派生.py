# 派生

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(Person):
    def __init__(self, name, age, sex, score, major):
        super().__init__(name, age, sex)
        self.score = score
        self.major = major

    def learn(self):
        print(f"{self.name}的专业是 {self.major}, 成绩是 {self.score}")


lingjiang = Student("凌绛", 18, "女", 100, "计算机科学与技术")
lingjiang.learn()

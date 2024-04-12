# 继承

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def speak(self):
        print(f"{self.name}会说话")


class Teacher(Person):
    def teach(self):
        print(f"{self.name}会讲课")


class Student(Person):
    def study(self):
        print(f"{self.name}会学习")


teacher1 = Teacher("Tom", 30, 'male')
teacher1.teach()
teacher1.speak()

student1 = Student('Marry', 18, 'female')
student1.study()
student1.speak()


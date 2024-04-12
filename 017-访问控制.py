# 访问控制

class Person:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        print(f"{self.name} 的成绩是 {self.__score}")

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("输入成绩有误，请重新设置")


wutinghan = Person('吴听寒', 100)
wutinghan.get_score()

# wutinghan.score = -100
# print(wutinghan.score)
# wutinghan.__score = -90
# wutinghan.set_score(-100)
print(wutinghan._Person__score)
# wutinghan.get_score()

